// Create socket for data transfer
var thisURL = location.protocol + '//' + document.domain + (location.port ? ':' + location.port : '');
var socket = io.connect(thisURL);

// When connected, start the handshake with an 'offer'
socket.on('connect', function(){
    socket.emit('handshake_from_client', {'key': 'hand'});
});

// Connection is confirmed
socket.on('handshake_to_client', function(response) {
    if(response.key == 'shake'){
        alert('connected!');
    }
});
