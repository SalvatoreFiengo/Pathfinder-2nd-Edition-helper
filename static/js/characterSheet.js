anchestrySelect = document.getElementById("anchestry");
anchestryForm = document.getElementById("anchestryForm");

anchestrySelect.addEventListener("change",function(){
    anchestry = anchestrySelect.value
    if( anchestry != undefined && anchestry != null){
        return anchestryForm.submit();
    }else{
        alert("error in submitting form named "+anchestrySelect.id)
    }
})
