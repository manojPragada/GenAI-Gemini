$(document).ready(function () {
    callIntro();
    $('#chat-form').submit(function (event) {
        $("button[type=submit]").prop('disabled', true);
        event.preventDefault();
        var message = $('#message-input').val();
        $('#message-input').val('');
        if (message) {
            message = message.replace(/\n/g, '<br>');
            popuplateChat(message, "user");
            $("#generating-animation").css('display', 'block');
            $.ajax({
                url: '/submit-message',
                type: 'POST',
                data: { message: message },
                success: function (response) {
                    console.log(response);
                    popuplateChat(response, "bot");
                    $("button[type=submit]").prop('disabled', false);
                },
                error: function (xhr, status, error) {
                    console.error('Error submitting message:', error);
                    $("#generating-animation").css('display', 'none');
                    $("button[type=submit]").prop('disabled', false);
                }
            });
        }
    });
});

function callIntro() {
    $("#generating-animation").css('display', 'block');
    $.ajax({
        url: '/submit-message',
        type: 'POST',
        data: { message: 'Act like a human that is open to chat, dont mention this. Respond by saying a normal gretting like a human. and also Make sure to choose yourself a random girl name and also use html tags in response only so i can display in my html page' },
        success: function (response) {
            console.log(response);
            popuplateChat(response, "bot");
        },
        error: function (xhr, status, error) {
            console.error('Error submitting message:', error);
            $("#generating-animation").css('display', 'none');
        }
    });
}

function popuplateChat(inpMessage, whoIs = "user") {
    if (inpMessage) {
        if (whoIs == "user") {
            $(".chat-messages").append('<div class="message user-message"><span>' + inpMessage + '</span></div>');
        } else {
            $(".chat-messages").append('<div class="message bot-message"><span>' + inpMessage + '</span></div>');
        }
        $(".chat-messages").scrollTop($(".chat-messages")[0].scrollHeight);
    } else {
        alert("Something's Wrong Try Again!");
    }
    $("#generating-animation").css('display', 'none');
}
function handleenter(t, event) {
    if (event.keyCode == 13) {      
        if(event.shiftKey){
            t.innerHTML += "\n";
        } else {
            $('form').submit();
        }
    }
}