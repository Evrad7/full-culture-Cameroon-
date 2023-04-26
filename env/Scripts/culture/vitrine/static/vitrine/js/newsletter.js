document.addEventListener("DOMContentLoaded", function(){
    document.querySelector("form.newsletter").addEventListener("submit", function(e){
        e.preventDefault()
        sendDataAjax(new FormData(e.target), e.target.action)
    })

})

function sendDataAjax(data, url){
    var xhr=new XMLHttpRequest()
    xhr.open("POST", url, true)
    xhr.responseType="json"    
    xhr.onloadstart=function(){
        document.querySelector("form.newsletter button").innerHTML="\
        <span class='spinner-border spinner-border-sm me-1' role='status' aria-hidden='true'></span>\
        Abonnement..."
    }
    xhr.onloadend=function(){
        document.querySelector("form.newsletter button").innerHTML="\
        S'abonner"
    }
    xhr.send(data)

    xhr.onload=function(){
        if(xhr.status===200){
            document.querySelector("form.newsletter .info").innerHTML=""
            infoElement=document.querySelector("form.newsletter .info")
            if(xhr.response.errors!==null){
                xhr.response.errors.email.forEach(function(error){
                    infoElement.innerHTML+="\
                    <small class='text-danger fs-6'>"+error+"</small> <br\>"
                });
            }
            else{
                infoElement.innerHTML="\
                <small class='text-success fs-6 '>"+xhr.response.message+"</small>"
                document.querySelector(".alert-container").innerHTML="\
                <div class='alert alert-success alert-dismissible fade show' role='alert'>\
                <i class='bi bi-check-circle-fill'></i>\
                 <strong>"+xhr.response.message+"</strong> \
                <button type='button' class='btn-close' data-bs-dismiss='alert' aria-label='Close'></button>\
                </div>"
            }
           
        }
        else{
            document.querySelector(".alert-container").innerHTML="\
            <div class='alert alert-warning alert-dismissible fade show' role='alert'>\
            <i class='bi bi-exclamation-circle-fill'></i>\
             Une erreur est survenue \
            <button type='button' class='btn-close' data-bs-dismiss='alert' aria-label='Close'></button>\
            </div>"
        }
  
    }
    xhr.onerror=function(){
        document.querySelector(".alert-container").innerHTML="\
            <div class='alert alert-danger alert-dismissible fade show' role='alert'>\
            <i class='bi bi-exclamation-diamond-fill'></i>\
             Une erreur de connection  réseau est survenue \
            <button type='button' class='btn-close' data-bs-dismiss='alert' aria-label='Close'></button>\
            </div>"
    }
    
}