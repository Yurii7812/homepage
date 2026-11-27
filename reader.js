(() => {
  "use strict";
  const root = new URL(".", location.href);
  const rootPath = root.pathname;
  const content = document.getElementById("content");
  const nav = document.getElementById("site-nav");
  const paperCss = document.getElementById("paper-css");
  let currentFile = "", generation = 0;
  const valid = p => /^(ja|en)\/(?:[a-zA-Z0-9_-]+\/)*[a-zA-Z0-9_-]+\.md$/.test(p);
  const hashFor = (file, section = "") => "#/" + file + (section ? "?section=" + encodeURIComponent(section) : "");
  function savedLanguage() {
    const lang = new URL(location.href).searchParams.get("lang");
    if (lang === "ja" || lang === "en") return lang;
    try { return localStorage.getItem("lang") === "en" ? "en" : "ja"; } catch { return "ja"; }
  }
  function route() {
    const raw = location.hash.startsWith("#/") ? location.hash.slice(2) : "";
    const [file, query = ""] = raw.split("?", 2);
    if (!valid(file)) return { file: savedLanguage() + "/home.md", section: "" };
    return { file, section: new URLSearchParams(query).get("section") || "" };
  }
  function setNav(file) {
    const lang = file.split("/")[0], rest = file.slice(3);
    const paired = /^(home\.md|archive\.md|paper-pkm\/guide\.md|yuriinote\/guide\.md)$/.test(rest);
    document.documentElement.lang = lang;
    try { localStorage.setItem("lang", lang); } catch {}
    nav.replaceChildren();
    const home = document.createElement("a");
    home.href = hashFor(lang + "/home.md");
    home.textContent = lang === "ja" ? "ホーム" : "Home";
    nav.append(home);
    const langs = document.createElement("span");
    langs.className = "languages";
    for (const l of ["ja", "en"]) {
      const a = document.createElement("a");
      a.href = hashFor(l + "/" + (paired ? rest : "home.md"));
      a.textContent = l === "ja" ? "日本語" : "English";
      a.lang = l;
      if (l === lang) a.setAttribute("aria-current", "page");
      langs.append(a);
    }
    nav.append(langs);
  }
  function rewriteLinks(fragment, file) {
    const base = new URL(file, root);
    const ids = new Set(Array.from(fragment.querySelectorAll("[id]"), e => e.id));
    for (const h of fragment.querySelectorAll("h1,h2,h3,h4,h5,h6")) {
      if (!h.id) {
        let id = h.textContent.trim().toLowerCase().replace(/[^\p{L}\p{N}\s_-]/gu, "").replace(/\s+/g, "-") || "section";
        const stem = id; let n = 2; while (ids.has(id)) id = stem + "-" + n++;
        h.id = id; ids.add(id);
      }
    }
    for (const a of fragment.querySelectorAll("a[href]")) {
      const raw = a.getAttribute("href");
      if (raw.startsWith("#")) {
        let section = raw.slice(1); try { section = decodeURIComponent(section); } catch {}
        a.href = hashFor(file, section);
        continue;
      }
      const url = new URL(raw, base);
      const relative = url.origin === root.origin && url.pathname.startsWith(rootPath) ? url.pathname.slice(rootPath.length) : "";
      if (valid(relative)) {
        let section = url.hash.slice(1); try { section = decodeURIComponent(section); } catch {}
        a.href = hashFor(relative, section);
      } else a.href = url.href;
    }
    for (const img of fragment.querySelectorAll("img[src]")) {
      img.src = new URL(img.getAttribute("src"), base).href;
      img.loading = "lazy";
    }
    for (const table of fragment.querySelectorAll("table")) {
      const wrapper = document.createElement("div"); wrapper.className = "table-wrap";
      table.replaceWith(wrapper); wrapper.append(table);
    }
  }
  function scrollToSection(section) {
    if (section) document.getElementById(section)?.scrollIntoView();
    else window.scrollTo(0, 0);
  }
  async function render() {
    const { file, section } = route();
    if (!location.hash.startsWith("#/") || location.hash.slice(2).split("?")[0] !== file) {
      history.replaceState(null, "", root.href + hashFor(file, section));
    }
    if (file === currentFile) { scrollToSection(section); return; }
    const serial = ++generation, ja = file.startsWith("ja/");
    setNav(file);
    paperCss.disabled = !file.includes("/paper-pkm/");
    content.className = file.includes("/paper-pkm/") ? "paper-guide" : file.endsWith("/home.md") ? "home" : "article";
    content.setAttribute("aria-busy", "true");
    content.textContent = ja ? "読み込み中…" : "Loading…";
    try {
      if (!window.marked || !window.DOMPurify) throw new Error("Markdown renderer unavailable");
      const response = await fetch(new URL(file, root), { cache: "no-cache" });
      if (!response.ok) throw new Error("HTTP " + response.status);
      const source = await response.text();
      if (serial !== generation) return;
      const fragment = DOMPurify.sanitize(marked.parse(source, { gfm: true }), { RETURN_DOM_FRAGMENT: true, USE_PROFILES: { html: true } });
      rewriteLinks(fragment, file);
      content.replaceChildren(fragment);
      currentFile = file;
      document.title = (content.querySelector("h1")?.textContent || "Yurii") + " | Yurii";
      scrollToSection(section);
    } catch (error) {
      if (serial !== generation) return;
      currentFile = "";
      content.textContent = ja ? "ページを読み込めませんでした。再読み込みしてください。" : "Could not load this page. Please reload.";
      console.error(error);
    } finally { if (serial === generation) content.removeAttribute("aria-busy"); }
  }
  window.addEventListener("hashchange", render);
  render();
})();
