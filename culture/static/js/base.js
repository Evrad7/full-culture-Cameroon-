window.addEventListener("load", function(){
    ScrollReveal().reveal('.scrollreveal-text', {duration:800, distance:"30px", reset:true, delay:300, easing:'cubic-bezier(0.5, 0, 0, 1)', viewFactor:.0});
    ScrollReveal().reveal('.scrollreveal-img',{duration:800, distance:"30px", reset:true, easing: 'cubic-bezier(0.5, 0, 0, 1)', viewFactor:.0});
    ScrollReveal().reveal('.scrollreveal-home-text', {duration:800, distance:"300px",  delay:500, easing:'cubic-bezier(0.5, 0, 0, 1)', viewFactor:.2, origin:"left"});
    ScrollReveal().reveal('.scrollreveal-home-img', {duration:800, distance:"300px",  delay:500, easing:'cubic-bezier(0.5, 0, 0, 1)', viewFactor:.2, origin:"right"});


}
)