let loadComments = function () {
    let buttonElement = '<button class="btn btn-success fixed-bottom m-4" data-toggle="modal" data-target="#exampleModal">Comment</button>';
    $('#idCommentButton').append(buttonElement);

    let requestData = {
        // TODO: change on window.location.href
        url: window.location.pathname
    };
    $.ajax({
        url: 'http://localhost:8000/comment/api/comments/html/',
        method: 'POST',
        data: requestData,
        dataType: 'html',
        success: function (htmlData) {
            $('body').append(htmlData);
        },
    })
};

window.onload = function (event) {
    if (!window.jQuery) {
        let script = document.createElement('script');
        script.type = "text/javascript";
        script.src = "https://code.jquery.com/jquery-3.3.1.js";
        script.integrity = 'sha256-2Kok7MbOyxpgUVvAk/HJ2jigOSYS2auK4Pfzbm7uH60=';
        script.crossOrigin = 'anonymous';
        document.body.appendChild(script);
        script.onload = loadComments;
    }
    else {
        loadComments();
    }
};
