(() => {
"use strict";
const content = document.getElementById("content");
const root = new URL(".", location.href);
const mapPath = /\/ja\/brainstorm-philosophy\/figures\/(?:overview|chapter[1-4]|benefits)\.svg$/;
const isMap = img => img instanceof HTMLImageElement && mapPath.test(new URL(img.src, location.href).pathname) && new URL(img.src, location.href).origin === location.origin;
const style = document.createElement("style");
style.textContent = '.map-zoom-trigger{cursor:zoom-in!important}.network-dialog{box-sizing:border-box;width:96vw;max-width:none;height:94vh;height:94dvh;max-height:none;padding:0;border:1px solid #777;border-radius:6px;background:#fff;color:#222;overflow:hidden}.network-dialog[open]{display:flex;flex-direction:column}.network-dialog::backdrop{background:#0009}.network-toolbar{display:flex;align-items:center;gap:8px;padding:8px 12px;border-bottom:1px solid #ddd;flex-wrap:wrap}.network-toolbar button{font:inherit;min-width:42px;padding:6px 10px;border:1px solid #aaa;border-radius:4px;background:#fff;color:#222;cursor:pointer}.network-toolbar button:focus-visible{outline:2px solid #005bcc}.network-toolbar .network-close{margin-left:auto}.network-hint{font-size:12px;color:#555}.network-stage{position:relative;flex:1;min-height:0;overflow:auto;overscroll-behavior:contain;background:#fff;touch-action:none;cursor:grab}.network-stage.dragging{cursor:grabbing;user-select:none}.network-canvas{position:relative;display:flex;align-items:center;justify-content:center}.network-canvas svg{display:block;flex:none;max-width:none!important;max-height:none!important}.network-canvas svg a{cursor:pointer}.network-canvas svg a:hover text,.network-canvas svg a:focus text{fill:#005bcc;text-decoration:underline}.network-stage:focus-visible{outline:2px solid #005bcc;outline-offset:-2px}';
document.head.append(style);
const dlg=document.createElement("dialog");dlg.className="network-dialog";dlg.setAttribute("aria-label","網状図の拡大表示");
dlg.innerHTML='<div class="network-toolbar"><button type="button" data-cmd="minus" aria-label="縮小">−</button><button type="button" data-cmd="plus" aria-label="拡大">＋</button><button type="button" data-cmd="fit">全体表示</button><span class="network-level" aria-live="polite"></span><span class="network-hint">ホイール／ピンチ：ズーム　ドラッグ：移動　文字：本文へ</span><button type="button" data-cmd="close" class="network-close" aria-label="閉じる">閉じる ×</button></div><div class="network-stage" tabindex="0"><div class="network-canvas"></div></div>';
document.body.append(dlg);
const stage=dlg.querySelector(".network-stage"),canvas=dlg.querySelector(".network-canvas"),level=dlg.querySelector(".network-level");
let svg=null,vw=1,vh=1,scale=1,fit=1,serial=0,trigger=null,oldOverflow="",suppressUntil=0,dragged=false;
const pointers=new Map();
function dimensions(){
  if(!svg)return;
  const w=vw*scale,h=vh*scale;
  svg.style.width=w+"px";svg.style.height=h+"px";
  canvas.style.width=Math.max(stage.clientWidth,w)+"px";
  canvas.style.height=Math.max(stage.clientHeight,h)+"px";
  level.textContent=Math.round(scale*100)+"%";
}
function centerPoint(){const r=stage.getBoundingClientRect();return [r.left+stage.clientWidth/2,r.top+stage.clientHeight/2];}
function zoom(next,px,py){
  if(!svg)return;
  const old=svg.getBoundingClientRect(),sr=stage.getBoundingClientRect();
  const fx=(px-old.left)/old.width,fy=(py-old.top)/old.height;
  scale=Math.max(fit*.5,Math.min(Math.max(fit*20,5),next));dimensions();
  stage.scrollLeft=svg.offsetLeft+fx*vw*scale-(px-sr.left);
  stage.scrollTop=svg.offsetTop+fy*vh*scale-(py-sr.top);
}
function reset(){if(!svg)return;fit=Math.min((stage.clientWidth-16)/vw,(stage.clientHeight-16)/vh);fit=Math.max(.01,fit);scale=fit;dimensions();stage.scrollLeft=0;stage.scrollTop=0;}
function jump(id){
  if(!/^bm-[a-z0-9-]+$/.test(id))return;
  dlg.close();
  const h="#/ja/brainstorm-philosophy/guide.md?section="+encodeURIComponent(id);
  if(location.hash===h)document.getElementById(id)?.scrollIntoView();
  else location.hash=h;
}
async function openMap(img){
  const token=++serial;trigger=img;svg=null;canvas.replaceChildren();level.textContent="";pointers.clear();
  if(!dlg.open){oldOverflow=document.body.style.overflow;document.body.style.overflow="hidden";dlg.showModal();}
  canvas.textContent="読み込み中…";
  try{
    const res=await fetch(img.src,{cache:"no-cache"});if(!res.ok)throw Error("HTTP "+res.status);
    const raw=await res.text();if(token!==serial||!dlg.open)return;
    const clean=DOMPurify.sanitize(raw,{USE_PROFILES:{svg:true,svgFilters:false},ADD_TAGS:["a"],ADD_ATTR:["data-section","tabindex"],FORBID_TAGS:["script","foreignObject","style"],FORBID_ATTR:["style"]});
    const doc=new DOMParser().parseFromString(clean,"image/svg+xml"),node=doc.documentElement;
    if(node.localName!=="svg"||doc.querySelector("parsererror"))throw Error("Invalid SVG");
    svg=document.importNode(node,true);
    const vb=svg.getAttribute("viewBox").trim().split(/[\s,]+/).map(Number);
    if(vb.length!==4||!Number.isFinite(vb[2])||!Number.isFinite(vb[3])||vb[2]<=0||vb[3]<=0)throw Error("Invalid viewBox");
    vw=vb[2];vh=vb[3];
    svg.setAttribute("aria-label",img.alt||"網状図");svg.removeAttribute("role");
    // Only local article destinations are interactive in the viewer.
    svg.querySelectorAll("a").forEach(a=>{a.removeAttribute("href");a.removeAttributeNS("http://www.w3.org/1999/xlink","href");if(/^bm-[a-z0-9-]+$/.test(a.dataset.section||"")){a.setAttribute("role","link");a.setAttribute("tabindex","0");}else a.removeAttribute("tabindex");});
    canvas.replaceChildren(svg);reset();stage.focus({preventScroll:true});
  }catch(e){if(token===serial&&dlg.open){svg=null;canvas.textContent="図を読み込めませんでした。閉じて再試行してください。";console.error(e);}}
}
function decorate(){content.querySelectorAll("img").forEach(img=>{if(isMap(img)){img.classList.add("map-zoom-trigger");img.setAttribute("tabindex","0");img.setAttribute("role","button");img.title="クリックして拡大・本文へ移動";}});}
new MutationObserver(decorate).observe(content,{childList:true,subtree:true});decorate();
content.addEventListener("click",e=>{if(isMap(e.target)){e.preventDefault();openMap(e.target);}});
content.addEventListener("keydown",e=>{if(isMap(e.target)&&(e.key==="Enter"||e.key===" ")){e.preventDefault();openMap(e.target);}});
dlg.addEventListener("close",()=>{++serial;svg=null;pointers.clear();stage.classList.remove("dragging");document.body.style.overflow=oldOverflow;if(trigger?.isConnected)trigger.focus({preventScroll:true});});
dlg.addEventListener("click",e=>{
  const cmd=e.target.closest("button")?.dataset.cmd;
  if(cmd==="close"){dlg.close();return;}if(cmd==="fit"){reset();return;}
  if(cmd==="plus"||cmd==="minus"){zoom(scale*(cmd==="plus"?1.25:.8),...centerPoint());return;}
  const a=e.target.closest("[data-section]");if(a&&performance.now()>suppressUntil){e.preventDefault();jump(a.dataset.section);}
});
dlg.addEventListener("keydown",e=>{
  const a=e.target.closest?.("[data-section]");if(a&&(e.key==="Enter"||e.key===" ")){e.preventDefault();jump(a.dataset.section);return;}
  if(e.key==="+"||e.key==="="||e.key==="-"){e.preventDefault();zoom(scale*(e.key==="-"?.8:1.25),...centerPoint());}
  else if(e.key==="0"){e.preventDefault();reset();}
});
stage.addEventListener("wheel",e=>{if(!svg)return;e.preventDefault();zoom(scale*Math.exp(-Math.max(-120,Math.min(120,e.deltaY))*.003),e.clientX,e.clientY);},{passive:false});
stage.addEventListener("pointerdown",e=>{if(!svg||e.button!==0)return;if(!pointers.size)dragged=false;pointers.set(e.pointerId,{x:e.clientX,y:e.clientY});if(pointers.size>1){dragged=true;for(const id of pointers.keys())try{stage.setPointerCapture(id);}catch{};stage.classList.add("dragging");}});
stage.addEventListener("pointermove",e=>{
  if(!pointers.has(e.pointerId))return;
  const old=pointers.get(e.pointerId),next={x:e.clientX,y:e.clientY};
  if(pointers.size>=2){const other=[...pointers.entries()].find(([id])=>id!==e.pointerId)[1];const d0=Math.hypot(old.x-other.x,old.y-other.y),d1=Math.hypot(next.x-other.x,next.y-other.y);if(d0>4){zoom(scale*d1/d0,(next.x+other.x)/2,(next.y+other.y)/2);}dragged=true;}
  else if(dragged||Math.hypot(next.x-old.x,next.y-old.y)>4){dragged=true;stage.classList.add("dragging");try{stage.setPointerCapture(e.pointerId);}catch{}stage.scrollLeft-=next.x-old.x;stage.scrollTop-=next.y-old.y;}
  else return;
  pointers.set(e.pointerId,next);
});
function endPointer(e){if(!pointers.has(e.pointerId))return;pointers.delete(e.pointerId);if(dragged)suppressUntil=performance.now()+350;if(!pointers.size){stage.classList.remove("dragging");dragged=false;}}
stage.addEventListener("pointerup",endPointer);stage.addEventListener("pointercancel",endPointer);stage.addEventListener("lostpointercapture",endPointer);
window.addEventListener("resize",()=>{if(dlg.open&&svg){fit=Math.max(.01,Math.min((stage.clientWidth-16)/vw,(stage.clientHeight-16)/vh));dimensions();}});
window.addEventListener("hashchange",()=>{if(dlg.open)dlg.close();});
})();