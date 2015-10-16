/* application/static/js/socket.js */
// Do synchronous AJAX call to ask for username
var initial_player_data = {};
$.ajax({
    type: 'POST',
    dataType: 'json',
    async: false,
    success: function(response){
        initial_player_data.username = response.username;
        initial_player_data.x = response.x;
        initial_player_data.y = response.y;
    }
});

// Create socket AFTER we have the username to sign our communications with
var thisURL = location.protocol + '//' + document.domain + (location.port ? ':' + location.port : '');
socket = io.connect(thisURL);

// On connect, request the rest of the data about the user
socket.on('connect', function(){
    socket.emit('handshake from client', {'key': 'hand'});
});

socket.on('handshake to client', function(response){
    if(response.key == 'shake'){
        alert('connected!');
    }
});
