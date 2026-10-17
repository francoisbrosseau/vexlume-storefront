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
