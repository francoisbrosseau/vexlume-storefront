const fs=require('node:fs'),vm=require('node:vm'),assert=require('node:assert/strict');
function element(data={}){return{dataset:data,hidden:false,attrs:{},listeners:{},classList:{state:new Set(),toggle(c,on){if(on)this.state.add(c);else this.state.delete(c);},remove(c){this.state.delete(c);}},setAttribute(k,v){this.attrs[k]=v;},getAttribute(k){return this.attrs[k];},addEventListener(e,fn){this.listeners[e]=fn;},focus(){this.focused=true;}};}
const toggle=element();toggle.attrs['aria-expanded']='false';const nav=element();const search=element();search.value='';const count=element(),empty=element();
const filters=['all','Home & space','Money & planning'].map(filter=>element({filter}));
const cards=[element({title:'the picture-perfect property',category:'Home & space'}),element({title:'the financial clarity kit',category:'Money & planning'}),element({title:'the weekly reset planner',category:'Everyday rituals'})];
const map={'.menu-toggle':toggle,'#navigation':nav,'#product-search':search,'#catalog-count':count,'#empty-state':empty};
const document={listeners:{},querySelector:s=>map[s],querySelectorAll:s=>s==='[data-filter]'?filters:cards,addEventListener(e,fn){this.listeners[e]=fn;}};
vm.runInNewContext(fs.readFileSync(require('node:path').join(__dirname,'../dist/assets/app.js'),'utf8'),{document});
toggle.listeners.click();assert.equal(toggle.attrs['aria-expanded'],'true');assert(nav.classList.state.has('open'));
document.listeners.keydown({key:'Escape'});assert.equal(toggle.attrs['aria-expanded'],'false');assert(toggle.focused);
filters[1].listeners.click();assert.deepEqual(cards.map(c=>c.hidden),[false,true,true]);assert.equal(count.textContent,'1 tool in the collection');
search.value='nonexistent';search.listeners.input();assert(cards.every(c=>c.hidden));assert.equal(empty.hidden,false);
filters[0].listeners.click();search.value='  PLANNER  ';search.listeners.input();assert.deepEqual(cards.map(c=>c.hidden),[true,true,false]);assert.equal(empty.hidden,true);
search.value='';search.listeners.input();assert(cards.every(c=>!c.hidden));assert.equal(count.textContent,'3 tools in the collection');
console.log('PASS: menu open/escape/focus; category filter; combined search; zero state; case/whitespace; reset. Browser layout remains unverified.');
