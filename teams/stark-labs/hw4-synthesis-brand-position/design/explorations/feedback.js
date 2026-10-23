
(() => {
 const form=document.querySelector('[data-feedback]'); if(!form)return;
 const id=form.dataset.feedback, key='clientready-design-feedback-'+id;
 const status=document.querySelector('[role="status"]');
 let record={}; try{record=JSON.parse(localStorage.getItem(key)||'{}')}catch(e){}
 for(const [name,value] of Object.entries(record)) if(form.elements[name])form.elements[name].value=value;
 const data=()=>({direction:id,reviewer:form.elements.reviewer.value,decision:form.elements.decision.value,keep:form.elements.keep.value,kill:form.elements.kill.value,why:form.elements.why.value,recorded_at:new Date().toISOString(),provenance:'User-entered design feedback; empty fields are not decisions.'});
 form.addEventListener('submit',e=>{e.preventDefault();try{localStorage.setItem(key,JSON.stringify(data()));status.textContent='Saved in this browser. Export a copy to share with your team.'}catch(e){status.textContent='Browser storage is unavailable. Export a copy instead.'}});
 form.querySelector('[data-export]').addEventListener('click',()=>{const a=document.createElement('a');a.href=URL.createObjectURL(new Blob([JSON.stringify(data(),null,2)],{type:'application/json'}));a.download=id+'-feedback.json';a.click();setTimeout(()=>URL.revokeObjectURL(a.href),2000);status.textContent='Feedback exported. Save the file with your assignment materials.'});
})();
