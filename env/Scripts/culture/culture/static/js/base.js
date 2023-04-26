document.addEventListener("DOMContentLoaded", function(){
    console.log("---------------------------------------")
    ScrollReveal().reveal('.scrollreveal-img',{duration:1000, distance:"100px", opacity:.5, reset:true});
    ScrollReveal().reveal('.scrollreveal-text', {duration:1000, distance:"100px", opacity:.8, reset:true});
    console.log("-----------------------------------")
    console.log(document.querySelectorAll(".scrollreveal-img"))
})