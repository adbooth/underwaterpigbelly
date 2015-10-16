var game = new Phaser.Game(800, 600, Phaser.AUTO, '', { preload: preload, create: create, update: update });

var username = initial_player_data.username;

function preload() {
    game.load.image('blue-circle', '/static/assets/circle-32.ico');
    game.load.image('red-circle', '/static/assets/circle-32.gif');
}

var username = initial_player_data.username;
var protagonist;
var players;
var cursors;

function create() {
    // Some sort of necessary physics engine
    game.physics.startSystem(Phaser.Physics.ARCADE);

    // Protagonist creation
    protagonist = game.add.sprite(initial_player_data.x, initial_player_data.y, 'blue-circle');
    protagonist.name = username;
    game.physics.arcade.enable(protagonist);
    protagonist.body.collideWorldBounds = true;

    // I/O creation
    cursors = game.input.keyboard.createCursorKeys();

    // Other player data structure
    players = game.add.group();
    players.enableBody = true;
}

function update() {
    // game.physics.arcade.collide(players, players);

    // Moves protagonist based on input
    protagonist.body.velocity.x = 0;
    protagonist.body.velocity.y = 0;
    if(cursors.left.isDown){
        protagonist.body.velocity.x -= 150;
    }
    if(cursors.right.isDown){
        protagonist.body.velocity.x += 150;
    }
    if(cursors.up.isDown){
        protagonist.body.velocity.y -= 150;
    }
    if(cursors.down.isDown){
        protagonist.body.velocity.y += 150;
    }

    socket.emit('location update', {
        'username': username,
        'x': protagonist.x,
        'y': protagonist.y
    });
}

socket.on('player added', function(message){
    opponent = players.create(message.x, message.y, 'red-circle');
    opponent.name = message.username;
});

socket.on('game update', function(message){
    players.forEach(function(player){
        if(player.name != username){
            player.x = message[player.name].x;
            player.y = message[player.name].y;
        }
    }, this);
});
