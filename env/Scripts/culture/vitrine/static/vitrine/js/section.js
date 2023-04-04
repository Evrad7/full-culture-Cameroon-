document.addEventListener("DOMContentLoaded", function(){
    new Glider(document.querySelector("#glider-1"), {
        slidesToShow:3,
        scrollLock:true,
        scrollLockDelay:1000,
        draggable:true,
        dragVelocity:.75,
        dragVelocity:1,
        scrollPropagate:true,
        resizeLock:false,
        arrows: {
            prev: '.glider-prev-1',
            next: '.glider-next-1'
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

    new Glider(document.querySelector("#glider-2"), {
        slidesToShow:5,
        scrollLock:true,
        scrollLockDelay:1000,
        draggable:true,
        dragVelocity:.75,
        dragVelocity:1,
        arrows: {
            prev: '.glider-prev-2',
            next: '.glider-next-2'
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