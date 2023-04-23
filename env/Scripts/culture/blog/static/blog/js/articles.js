
document.addEventListener("DOMContentLoaded", function(){
    document.querySelectorAll(".sections >div").forEach(function(elt){
        elt.addEventListener("click", function(e){
            document.querySelector("form.search input[name='sector']").value=elt.getAttribute("slug")
            document.querySelector("form.search").submit()         
        })
    })

})



