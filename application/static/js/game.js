Crafty.init(window.innerWidth, window.innerHeight, document.getElementById('game'));

Crafty.e('2D, DOM, Color, Fourway')
    .attr({x: 0, y: 0, w: 100, h: 100})
    .color('#F00')
    .fourway(5)
    .bind('EnterFrame', function(eventData){
        socket.emit('player_location', {'x': this.x, 'y': this.y});
    });

socket.on('location_info', function(info){
    // $('#x').text(info.x);
    // $('#y').text(info.y);
    var xtag = document.getElementById('x');
    var ytag = document.getElementById('y');
    xtag.innerHTML = 'x: ' + info.x;
    ytag.innerHTML = 'y: ' + info.y;
});
