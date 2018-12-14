let loadComments = function () {
    let requestData = {
        url: window.location.pathname
    };
    $.get({
        url: 'http://localhost:8000/comment/api/comments/',
        data: requestData,
        dataType: "json",
        success: function (data) {
            alert(data);
        }
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
