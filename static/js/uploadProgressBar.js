$("form").on("submit", (form) => {
    form.preventDefault()
    submitForm($(form.target), $(".progress"))
})

function submitForm(form, progressBar) {
    var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();

    $.ajax({
        xhr: function() {
            var xhr = new window.XMLHttpRequest();
            console.log("Sdasd")
            xhr.upload.addEventListener("progress", function(evt) {
            if (evt.lengthComputable) {
                progressBar.fadeIn()
                var percentComplete = evt.loaded / evt.total;
                percentComplete = parseInt(percentComplete * 100);
                console.log(percentComplete)
                progressBar.val(percentComplete)
    
                if (percentComplete === 100) {
                    progressBar.fadeOut()
                }
    
            }
            }, false);
    
            return xhr;
        },
        beforeSend: function (xhr){
            xhr.setRequestHeader('X-CSRFToken', csrftoken);
        },
        url: window.location.pathname+window.location.search,
        type: "POST",
        processData: false,
        contentType: false,
        data: new FormData(form[0]),
        success: function(result) {
            document.write(result)
        }
    });
}