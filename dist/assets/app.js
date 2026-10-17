'use strict';
const toggle=document.querySelector('.menu-toggle');
const nav=document.querySelector('#navigation');
if(toggle&&nav){
 toggle.addEventListener('click',()=>{const open=toggle.getAttribute('aria-expanded')!=='true';toggle.setAttribute('aria-expanded',String(open));nav.classList.toggle('open',open);});
 document.addEventListener('keydown',event=>{if(event.key==='Escape'&&toggle.getAttribute('aria-expanded')==='true'){toggle.setAttribute('aria-expanded','false');nav.classList.remove('open');toggle.focus();}});
}
const filters=[...document.querySelectorAll('[data-filter]')];
const search=document.querySelector('#product-search');
const cards=[...document.querySelectorAll('.catalog .product-card')];
let category='all';
function filterCatalog(){
 const term=(search?.value||'').toLocaleLowerCase().trim();let visible=0;
 cards.forEach(card=>{const match=(category==='all'||card.dataset.category===category)&&`${card.dataset.title} ${card.dataset.category}`.toLocaleLowerCase().includes(term);card.hidden=!match;if(match)visible++;});
 const count=document.querySelector('#catalog-count');if(count)count.textContent=`${visible} ${visible===1?'tool':'tools'} in the collection`;
 const empty=document.querySelector('#empty-state');if(empty)empty.hidden=visible!==0;
}
filters.forEach(button=>button.addEventListener('click',()=>{category=button.dataset.filter;filters.forEach(item=>item.setAttribute('aria-pressed',String(item===button)));filterCatalog();}));
if(search)search.addEventListener('input',filterCatalog);

// This exercise never sends answers or writes browser storage.
const stepForm=document.querySelector('#step-form');
if(stepForm){
 stepForm.addEventListener('submit',event=>{
  event.preventDefault();
  if(!stepForm.reportValidity())return;
  const fields=['focus','goal','action','when','review'];
  const values=Object.fromEntries(fields.map(name=>[name,document.querySelector(`#step-${name}`).value.trim()]));
  if(fields.some(name=>!values[name]))return;
  fields.forEach(name=>{document.querySelector(`#result-${name}`).textContent=values[name];});
  const result=document.querySelector('#step-result');result.hidden=false;result.focus();
 });
 document.querySelector('#print-step').addEventListener('click',()=>window.print());
}
