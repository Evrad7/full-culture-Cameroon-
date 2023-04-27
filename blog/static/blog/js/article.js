document.addEventListener("DOMContentLoaded", function(){
    document.querySelector("form.comment").addEventListener("submit", function(e){
        e.preventDefault()
        add_comment_ajax(new FormData(e.target), e.target.action)
    })
})

function add_comment_ajax(data, url){
    xhr=new XMLHttpRequest()
    xhr.open("POST", url, true)
    xhr.responseType="json"
    xhr.onloadstart=function(){
        document.querySelector("form.comment button").innerHTML="\
        <span class='spinner-border spinner-border-sm me-1' role='status' aria-hidden='true'></span>\
        Evoi..."
    }
    xhr.onloadend=function(){
        document.querySelector("form.comment button").innerHTML="\
        Envoyer"
    }
    xhr.send(data)

    xhr.onload=function(){
        if(xhr.status===200){
            author_errors_element=document.querySelector("input[name='author']").nextElementSibling
            content_errors_element=document.querySelector("textarea[name='content']").nextElementSibling
            author_errors_element.innerHTML=""
            content_errors_element.innerHTML=""
            if(xhr.response.errors!==null){
                if(xhr.response.errors.author!==undefined){
                    xhr.response.errors.author.forEach(function(error){
                        author_errors_element.innerHTML+="\
                        <small class='text-danger fs-6'>"+error+"</small> <br\>"
                    });
                }
                if(xhr.response.errors.content!==undefined){
                    xhr.response.errors.content.forEach(function(error){
                        content_errors_element.innerHTML+="\
                        <small class='text-danger fs-6'>"+error+"</small> <br\>"
                    });
                }
               
            }
            else{
                comment=xhr.response.comment
                comment_element=document.createElement("div")
                comment_form_element=document.querySelector("form.comment")
                comment_form_element.reset()
                comment_element.innerHTML="\
                <div class='mb-5'>\
                <div class='d-flex align-items-center mb-2'>\
                    <div class='rounded-circle border border-secondary p-1 bg-light'><i class='bi bi-person-fill fs-4 p-1'></i></div>\
                    <span class='ms-2 fs-6'>"+comment.author+"</span>\
                </div>\
                <p class='fs-5 text-secondary mb-1'>"+comment.content+"</p>\
                  <div class='text-end fst-italic'><span>"+comment.created_at+"</span></div>\
                  <hr>\
              </div>"
                comments_element=document.querySelector(".comments")
                if(comments_element.querySelector("form.coment")!==undefined){
                    comment_form_element.remove()
                    document.querySelector("#comment-box").prepend(comment_form_element)
                }
                comments_element.prepend(comment_element)
                document.querySelector(".alert-container").innerHTML="\
                <div class='alert alert-success alert-dismissible fade show' role='alert'>\
                <i class='bi bi-check-circle-fill'></i>\
                 <strong>Ajout de commentaire réussi.</strong> \
                <button type='button' class='btn-close' data-bs-dismiss='alert' aria-label='Close'></button>\
                </div>"
            }
               
        }
        else if(xhr.status===403){
            document.querySelector(".alert-container").innerHTML="\
            <div class='alert alert-warning alert-dismissible fade show' role='alert'>\
            <i class='bi bi-exclamation-diamond-fill'></i>\
                <strong>You can not write more than 03 comments per day</strong> \
            <button type='button' class='btn-close' data-bs-dismiss='alert' aria-label='Close'></button>\
            </div>"
        
        }
        else{
            document.querySelector(".alert-container").innerHTML="\
            <div class='alert alert-danger alert-dismissible fade show' role='alert'>\
            <i class='bi bi-exclamation-diamond-fill'></i>\
                <strong>Une erreur réseau .</strong> \
            <button type='button' class='btn-close' data-bs-dismiss='alert' aria-label='Close'></button>\
            </div>"
        }
    }
    xhr.onerror=function(){
        document.querySelector(".alert-container").innerHTML="\
        <div class='alert alert-danger alert-dismissible fade show' role='alert'>\
        <i class='bi bi-exclamation-diamond-fill'></i>\
         Erreur de réseau \
        <button type='button' class='btn-close' data-bs-dismiss='alert' aria-label='Close'></button>\
        </div>"
    }
}

