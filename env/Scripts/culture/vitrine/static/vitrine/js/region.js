document.addEventListener("DOMContentLoaded", function(){
    new Glider(document.querySelector(".glider"), {
        slidesToShow:3,
        scrollLock:true,
        scrollLockDelay:1000,
        draggable:true,
        dragVelocity:.75,
        dragVelocity:1,
        arrows: {
            prev: '.glider-prev',
            next: '.glider-next'
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