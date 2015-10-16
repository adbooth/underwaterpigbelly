/* application/static/js/game.js */
// Initialize game
Crafty.init(window.innerWidth, window.innerHeight, document.getElementById('game'));

// Create Crafty player component
Crafty.c('Player', {
    _username: '',
    init: function(){
        this.addComponent('2D, DOM, Color, Fourway');
        this.w = 50;
        this.h = 50;
        this.color('#F00');
    },
    Player: function(username){
        this.username = username;
        if(username == initial_player_data.username){
            this.fourway(5);
            this.x = initial_player_data.xpos;
            this.y = initial_player_data.ypos;
            this.bind('EnterFrame', function(){
                socket.emit('location update', {
                    'username': username,
                    'xpos': this.x,
                    'ypos': this.y
                });
            });
        }
    },
});

var player = Crafty.e('Player').Player(initial_player_data.username);

// On window close, send game close message
$(window).unload(function(){
    socket.emit('game close', {'username': username});
});
