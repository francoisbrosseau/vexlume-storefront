const vm=require('node:vm'),fs=require('node:fs'),assert=require('node:assert/strict');
function node(value=''){return{value,hidden:true,textContent:'',events:{},addEventListener(k,fn){this.events[k]=fn;},focus(){this.focused=true;}};}
const form=node();form.valid=true;form.reportValidity=()=>form.valid;
const result=node();const print=node();let prints=0,prevented=0;
const elements={'#step-form':form,'#step-result':result,'#print-step':print};
for(const key of ['focus','goal','action','when','review']){elements[`#step-${key}`]=node();elements[`#result-${key}`]=node();}
const document={querySelector:s=>elements[s],querySelectorAll:()=>[],addEventListener(){}};
vm.runInNewContext(fs.readFileSync(require('node:path').join(__dirname,'../dist/assets/app.js'),'utf8'),{document,window:{print(){prints++;}}});
const submit=()=>form.events.submit({preventDefault(){prevented++;}});
form.valid=false;submit();assert.equal(result.hidden,true);
form.valid=true;submit();assert.equal(result.hidden,true);
const values={focus:'Emotional clarity',goal:'  Understand a recurring feeling  ',action:'<img src=x onerror=alert(1)>',when:'Sunday after breakfast',review:'Next Sunday'};
for(const [key,value] of Object.entries(values))elements[`#step-${key}`].value=value;
submit();assert.equal(result.hidden,false);assert.equal(result.focused,true);assert.equal(elements['#result-goal'].textContent,'Understand a recurring feeling');assert.equal(elements['#result-action'].textContent,values.action);assert.equal(elements['#result-action'].innerHTML,undefined);
elements['#step-action'].value='Write for five minutes';submit();assert.equal(elements['#result-action'].textContent,'Write for five minutes');
print.events.click();assert.equal(prints,1);assert.equal(prevented,4);
console.log('PASS: invalid/empty input; trimmed answers; literal safe text; update action card; focus; print; submit prevention.');
