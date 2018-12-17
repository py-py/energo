let COMMENT_URL = 'http://localhost:8000/comment/api/comments/html/';

let CommentHandler = function () {
    let pr = {},
        pub = {};

    pr.getWindowHref = function () {
        return window.location.href
    };

    pr.addEventOnSendBlock = function () {
        $('#idCommentSendButton').click(function () {
            let data = {
                url: pr.getWindowHref(),
                text: $('#idCommentSendText').val()
            };

            $.ajax({
                url: COMMENT_URL,
                method: 'POST',
                data: data,
                dataType: 'html',
                success: function (data) {
                    $('#idCommentModalBodyList').prepend(data);
                    $('#idCommentSendText').val('');
                }
            })
        })
    };

    pr.createButton = function () {
        let buttonElement = '<button class="btn btn-success fixed-bottom m-4" data-toggle="modal" data-target="#idCommentModal">Comment</button>';
        $('#idCommentButton').append(buttonElement);
    };

    pr.loadComments = function () {
        let data = {
            url: pr.getWindowHref()
        };
        $.ajax({
            url: COMMENT_URL,
            method: 'GET',
            data: data,
            dataType: 'html',
            success: function (htmlData) {
                $('body').append(htmlData);
                pr.addEventOnSendBlock();
            },
        })
    };

    pub.run = function () {
        pr.createButton();
        pr.loadComments();
    };

    return pub;
};


window.onload = function (event) {
    commentHandler = CommentHandler();

    if (!window.jQuery) {
        alert('JQuery is not loaded!');
        // TODO: need to load bootstrap js files and need to styled button and modal window;
        // loadJQuery();
        // loadPopper();
        // let lastScript = loadBootstrap();
        // lastScript.onload = commentHandler.run();
    }
    else {
        commentHandler.run();
    }
};

// let loadJQuery = function () {
//     let scriptJQuery = document.createElement('script');
//     scriptJQuery.type = "text/javascript";
//     scriptJQuery.src = "https://code.jquery.com/jquery-3.3.1.js";
//     scriptJQuery.integrity = 'sha256-2Kok7MbOyxpgUVvAk/HJ2jigOSYS2auK4Pfzbm7uH60=';
//     scriptJQuery.crossOrigin = 'anonymous';
//     document.body.appendChild(scriptJQuery);
//     return scriptJQuery
// };
//
// let loadPopper = function () {
//     let scriptPopper = document.createElement('script');
//     scriptPopper.type = "text/javascript";
//     scriptPopper.src = "https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js";
//     scriptPopper.integrity = 'sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49';
//     scriptPopper.crossOrigin = 'anonymous';
//     document.body.appendChild(scriptPopper);
//     return scriptPopper;
// };
//
// let loadBootstrap = function () {
//     let scriptBootstrap = document.createElement('script');
//     scriptBootstrap.type = "text/javascript";
//     scriptBootstrap.src = "https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js";
//     scriptBootstrap.integrity = 'sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy';
//     scriptBootstrap.crossOrigin = 'anonymous';
//     document.body.appendChild(scriptBootstrap);
//     return scriptBootstrap;
// };
