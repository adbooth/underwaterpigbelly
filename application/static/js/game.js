Crafty.init(window.innerWidth, window.innerHeight, document.getElementById('game'));

Crafty.c('Player', {
    init: function(){
        this.addComponent('2D, DOM, Color, Fourway');
        this.x = 0;
        this.y = 0;
        this.w = 50;
        this.h = 50;
        this.color('#F00');
    }
});

var playerlist;
socketio.on('game update', function(message){
    player_data = message;
});

Crafty.bind('EnterFrame', function(){

});

var player = Crafty.e('Player');
player.fourway(5);
player.bind('EnterFrame', function(){
    socketio.emit('location update', {
        'username': username,
        'x': this.x,
        'y': this.y
    });
});

$(window).unload(function(){
    socketio.emit('game close', {'username': username});
});
