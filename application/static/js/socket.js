/* application/static/js/socket.js */
// Do synchronous AJAX call to ask for username
var initial_data = {};
$.ajax({
    type: 'POST',
    dataType: 'json',
    async: false,
    success: function(response){
        initial_data.username = response.username;
        initial_data.player_data = JSON.parse(response.player_data);
        initial_data.enemy_data = JSON.parse(response.enemy_data);
    }
});

// Create socket after we have the username to sign our communications with
var thisURL = location.protocol + '//' + document.domain + (location.port ? ':' + location.port : '');
socket = io.connect(thisURL);

// On connect, start handshake
socket.on('connect', function(){
    socket.emit('HANDSHAKE_FROM_CLIENT', {
        'username': initial_data.username,
        'payload': 'hand'
    });
});

// Confirm connection
socket.on('HANDSHAKE_TO_CLIENT', function(response){
    if(response.username == initial_data.username && response.payload == 'shake'){
        console.log('Connection confirmed.');
    }
});
