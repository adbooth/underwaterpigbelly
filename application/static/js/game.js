Crafty.init(window.innerWidth, window.innerHeight, document.getElementById('game'));

var player = Crafty.e('2D, DOM, Color, Fourway')
    .attr({x: 0, y: 0, w: 100, h: 100})
    .color('#F00')
    .fourway(5)
    .bind('EnterFrame', function(eventData){
        socket.emit('player_location', {'x': this.x, 'y': this.y});
    });

function addPlayer(){
    
}

// socket.on('location_info', function(info){
//     var xtag = document.getElementById('x').innerHTML = 'x: ' + info.x;
//     var ytag = document.getElementById('y').innerHTML = 'y: ' + info.y;
// });
