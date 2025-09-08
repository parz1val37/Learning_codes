from http.server import BaseHTTPRequestHandler, HTTPServer
import webbrowser

index_html = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>PARZi NOTES</title>
<style>
:root{--bg:#0f1724;--card:#0b1220;--muted:#9aa4b2;--accent:#7c3aed;--glass: rgba(255,255,255,0.03)}
html,body{height:100%;margin:0;font-family:Inter,system-ui,Arial;background:linear-gradient(180deg,#071024 0%,#081827 100%);color:#e6eef6}
.container{max-width:1100px;margin:28px auto;padding:22px}
.header{display:flex;align-items:center;justify-content:space-between}
.brand{display:flex;gap:14px;align-items:center}
.logo{width:48px;height:48px;border-radius:10px;background:linear-gradient(135deg,var(--accent),#2dd4bf);display:flex;align-items:center;justify-content:center;font-weight:700;color:white}
.title{font-size:1.2rem;font-weight:600}
.subtitle{color:var(--muted);font-size:0.85rem}
.layout{display:grid;grid-template-columns:360px 1fr;gap:18px;margin-top:18px}
.panel{background:var(--card);border-radius:12px;padding:14px;box-shadow:0 6px 18px rgba(2,6,23,0.6)}
.search{width:100%;padding:10px;border-radius:10px;border:0;background:var(--glass);color:inherit}
.notes-list{margin-top:12px;display:flex;flex-direction:column;gap:10px;max-height:68vh;overflow:auto;padding-right:6px}
.note-card{padding:12px;border-radius:10px;background:linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01));cursor:pointer;transition:0.2s}
.note-card:hover{background:rgba(124,58,237,0.1)}
.note-title{font-weight:600}
.note-snippet{color:var(--muted);font-size:0.85rem;margin-top:6px}
.editor{min-height:56vh;display:flex;flex-direction:column}
.toolbar{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:10px}
.btn{background:var(--glass);border:0;padding:8px 10px;border-radius:8px;cursor:pointer;color:inherit;transition:0.2s}
.btn:hover{background:rgba(124,58,237,0.15)}
.btn.active{background:rgba(124,58,237,0.25)}
.btn.primary{background:linear-gradient(90deg,var(--accent),#06b6d4);color:white}
.title-input{width:100%;padding:10px;border-radius:8px;border:0;background:transparent;color:inherit;font-size:1.05rem;font-weight:600}
.editable{flex:1;padding:12px;border-radius:10px;background:rgba(255,255,255,0.02);overflow:auto}
.small{font-size:0.85rem;color:var(--muted)}
.note-meta{display:flex;gap:10px;align-items:center}
.actions{display:flex;gap:8px}
@media (max-width:880px){.layout{grid-template-columns:1fr}.notes-list{max-height:26vh}}
</style>
</head>
<body>
<div class="container">
<div class="header">
<div class="brand"><div class="logo">
  <svg xmlns="http://www.w3.org/2000/svg" fill="white" viewBox="0 0 24 24" width="24" height="24">
    <path d="M19 2H5c-1.1 0-2 .9-2 2v16l4-4h12c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zm0 12H7l-2 2V4h14v10z"/>
  </svg></div><div><div class="title">PARZi NOTES</div><div class="subtitle">Local-first • Single-file</div></div></div>
<div><button id="new-note-btn" class="btn primary">New Note</button></div>
</div>
<div class="layout">
<div class="panel">
<input id="search" class="search" type="search" placeholder="Search for notes.."/>
<div id="notes-list" class="notes-list"></div>
</div>
<div class="panel editor">
<div class="note-meta"><input id="note-title" class="title-input" type="text" placeholder="Untitled note"/><div class="actions"><button id="save-btn" class="btn primary">Save</button><button id="delete-btn" class="btn">Delete</button></div></div>
<div class="toolbar">
<button id="fmt-bold" class="btn">B</button>
<button id="fmt-italic" class="btn">I</button>
<button id="fmt-underline" class="btn">U</button>
<button id="fmt-h1" class="btn">H1</button>
<button id="fmt-ul" class="btn">• List</button>
<button id="fmt-ol" class="btn">1. List</button>
<button id="fmt-link" class="btn">Link</button>
</div>
<div id="editor" class="editable" contenteditable="true" role="textbox" aria-label="Note editor"></div>
</div>
</div>
<div style="text-align:center;margin-top:14px;color:var(--muted);font-size:0.85rem;">Notes live in your browser (localStorage). No account needed.</div>
</div>
<script>
(function(){
const STORAGE_KEY='notes_v2';
const notesListEl=document.getElementById('notes-list');
const editorEl=document.getElementById('editor');
const titleEl=document.getElementById('note-title');
const searchEl=document.getElementById('search');
const newBtn=document.getElementById('new-note-btn');
const saveBtn=document.getElementById('save-btn');
const deleteBtn=document.getElementById('delete-btn');
let notes=[];
let activeId=null;
function nowISO(){return new Date().toISOString()}
function load(){try{const raw=localStorage.getItem(STORAGE_KEY);const parsed=raw?JSON.parse(raw):[];notes=Array.isArray(parsed)?parsed:[]}catch(e){notes=[]}}
function saveAll(){try{localStorage.setItem(STORAGE_KEY,JSON.stringify(notes))}catch(e){console.error('save failed',e)}}
function stripHtml(html){const d=document.createElement('div');d.innerHTML=html||'';return d.textContent||d.innerText||''}
function snippet(html){const txt=stripHtml(html).trim();return txt.length>120?txt.slice(0,120)+'...':(txt||'(empty)')}
function renderNotesList(filter){if(!notesListEl) return;notesListEl.innerHTML='';const f=String(filter||'').toLowerCase();const sorted=notes.slice().sort((a,b)=>new Date(b.updated_at||b.created_at)-new Date(a.updated_at||a.created_at));const filtered=sorted.filter(n=>((n.title||'').toLowerCase().includes(f))||((stripHtml(n.content)||'').toLowerCase().includes(f)));if(filtered.length===0){notesListEl.innerHTML='<div class="small" style="padding:8px;color:var(--muted)">No saved notes yet</div>';return}for(const n of filtered){const card=document.createElement('div');card.className='note-card';if(n.id===activeId) card.className+=' active-note';card.dataset.id=n.id;const t=document.createElement('div');t.className='note-title';t.innerText=n.title||'Untitled';const s=document.createElement('div');s.className='note-snippet';s.innerText=snippet(n.content);const meta=document.createElement('div');meta.className='small';meta.innerText=new Date(n.updated_at||n.created_at).toLocaleString();card.appendChild(t);card.appendChild(s);card.appendChild(meta);card.addEventListener('click',()=>openNote(n.id));notesListEl.appendChild(card)}}
function highlightActive(){const cards=document.querySelectorAll('.note-card');cards.forEach(c=>{c.style.outline=(c.dataset.id===activeId)?'2px solid rgba(124,58,237,0.18)':'none'})}
function createNoteWithContent(title,content){const id='n_'+Math.random().toString(36).slice(2,9);const now=nowISO();const n={id,title:title||'',content:content||'',created_at:now,updated_at:now};notes.push(n);saveAll();renderNotesList(searchEl?searchEl.value.toLowerCase():'');openNote(id);return n}
function newNote(){createNoteWithContent('','');if(titleEl) titleEl.focus()}
function openNote(id){const n=notes.find(x=>x.id===id);if(!n) return;activeId=id;if(titleEl) titleEl.value=n.title||'';if(editorEl) editorEl.innerHTML=n.content||'';highlightActive()}
function saveNote(){const title=(titleEl&&titleEl.value!==undefined)?titleEl.value.trim():'';const content=(editorEl&&editorEl.innerHTML!==undefined)?editorEl.innerHTML:'';if(!activeId){const created=createNoteWithContent(title,content);created.title=title;created.content=content;created.updated_at=nowISO();saveAll();renderNotesList(searchEl?searchEl.value.toLowerCase():'');activeId=created.id;flash('Saved');return}const n=notes.find(x=>x.id===activeId);if(!n){const created=createNoteWithContent(title,content);created.updated_at=nowISO();saveAll();renderNotesList(searchEl?searchEl.value.toLowerCase():'');activeId=created.id;flash('Saved');return}n.title=title;n.content=content;n.updated_at=nowISO();saveAll();renderNotesList(searchEl?searchEl.value.toLowerCase():'');flash('Saved')}
function deleteNote(){if(!activeId) return;const ok=confirm('Delete this note?');if(!ok) return;notes=notes.filter(x=>x.id!==activeId);saveAll();activeId=null;if(titleEl) titleEl.value='';if(editorEl) editorEl.innerHTML='';renderNotesList(searchEl?searchEl.value.toLowerCase():'');flash('Deleted')}
function flash(msg){const el=document.createElement('div');el.innerText=msg;el.style.position='fixed';el.style.right='18px';el.style.bottom='18px';el.style.padding='10px 12px';el.style.borderRadius='8px';el.style.background='rgba(0,0,0,0.6)';el.style.color='white';el.style.zIndex='9999';document.body.appendChild(el);setTimeout(()=>{el.style.transition='opacity 300ms';el.style.opacity='0'},1200);setTimeout(()=>el.remove(),1600)}
function format(cmd,val){try{document.execCommand(cmd,false,val)}catch(e){console.warn('format failed',e)}if(editorEl) editorEl.focus()}
function insertLink(){const url=prompt('Enter a URL (include https://)');if(!url) return;format('createLink',url)}
newBtn.addEventListener('click',()=>{newNote();if(titleEl) titleEl.focus()});if(saveBtn) saveBtn.addEventListener('click',saveNote);if(deleteBtn) deleteBtn.addEventListener('click',deleteNote);
[['fmt-bold','bold'],['fmt-italic','italic'],['fmt-underline','underline']].forEach(([id,cmd])=>{
    const el=document.getElementById(id);
    if(el) el.addEventListener('click',()=>{
        format(cmd);
        el.classList.toggle('active');
    })
});
const h1=document.getElementById('fmt-h1');if(h1) h1.addEventListener('click',()=>{format('formatBlock','<h1>');h1.classList.toggle('active')});
const fu=document.getElementById('fmt-ul');if(fu) fu.addEventListener('click',()=>{format('insertUnorderedList');fu.classList.toggle('active')});
const fo=document.getElementById('fmt-ol');if(fo) fo.addEventListener('click',()=>{format('insertOrderedList');fo.classList.toggle('active')});
const flink=document.getElementById('fmt-link');if(flink) flink.addEventListener('click',()=>{insertLink();flink.classList.toggle('active')});
let saveTimer=null;
function scheduleAutoSave(){if(saveTimer) clearTimeout(saveTimer);saveTimer=setTimeout(()=>{saveNote();saveTimer=null},900)}
if(editorEl) editorEl.addEventListener('input',scheduleAutoSave);
if(titleEl) titleEl.addEventListener('input',scheduleAutoSave);
if(searchEl) searchEl.addEventListener('input',e=>renderNotesList(String(e.target.value||'').toLowerCase()));
load();
renderNotesList();
if(notes.length){const last=notes.slice().sort((a,b)=>new Date(b.updated_at||b.created_at)-new Date(a.updated_at||a.created_at))[0];if(last) openNote(last.id)}
window.addEventListener('keydown',e=>{const mod=e.ctrlKey||e.metaKey;if(mod&&e.key&&e.key.toLowerCase()==='s'){e.preventDefault();saveNote()}if(mod&&e.key&&e.key.toLowerCase()==='n'){e.preventDefault();newNote()}});
window.NOTES_APP={get notes(){return notes},saveAll(){saveAll()}}
})();
</script>
</body>
</html>
"""

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path in ('/', '/index.html'):
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(index_html.encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

if __name__ == '__main__':
    port = 8000
    try:
        server = HTTPServer(('0.0.0.0', port), Handler)
        print(f'Serving at http://127.0.0.1:{port}')
        try:
            webbrowser.open(f'http://127.0.0.1:{port}')
        except Exception:
            pass
        server.serve_forever()
    except OSError as e:
        print('Port in use or permission denied:', e)