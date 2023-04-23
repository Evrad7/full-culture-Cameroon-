document.addEventListener("DOMContentLoaded", function(){
    document.querySelectorAll(".glider").forEach(function(elt){
        console.log(elt.id)
        index=elt.id.split("-")[1]
             new Glider(document.querySelector("#"+elt.id), {
        slidesToShow:3,
        scrollLock:true,
        scrollLockDelay:1000,
        draggable:true,
        dragVelocity:.75,
        dragVelocity:1,
        scrollPropagate:true,
        resizeLock:false,
        arrows: {
            prev: '.glider-prev-'+index,
            next: '.glider-next-'+index,
          },
          responsive:[
            {
                breakpoint:992,
                settings:{
                    slidesToShow:4
                }
            }
          ]
      
       
    })

})

})