// Native <dialog>: keyboard accessible, Escape closes, original figures stay intact.
document.addEventListener('DOMContentLoaded', () => {
  const ja=document.documentElement.lang==='ja';
  const dialog=document.createElement('dialog');dialog.className='guide-zoom';
  const close=document.createElement('button');close.className='guide-zoom-close';close.textContent=ja?'閉じる（Esc）':'Close (Esc)';
  const content=document.createElement('div');content.className='guide-zoom-content';dialog.append(close,content);document.body.append(dialog);
  close.onclick=()=>dialog.close();dialog.addEventListener('click',e=>{if(e.target===dialog)dialog.close();});
  document.querySelectorAll('figure[data-zoom]').forEach(figure=>{
    const button=document.createElement('button');button.className='zoom-button';button.textContent=ja?'図を拡大':'Enlarge figure';figure.append(button);
    const open=()=>{const clone=figure.cloneNode(true);clone.querySelectorAll('.zoom-button').forEach(x=>x.remove());clone.removeAttribute('id');clone.querySelectorAll('[id]').forEach(x=>x.removeAttribute('id'));content.replaceChildren(clone);dialog.showModal();close.focus();};
    figure.addEventListener('click',e=>{if(!e.target.closest('a'))open();});
  });
});
