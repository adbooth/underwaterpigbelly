var game = new Phaser.Game(800, 600, Phaser.AUTO, '', { preload: preload, create: create, update: update });

console.log(initial_data);
var username = initial_data.username;

function preload() {
    game.load.image('blue-circle', '/static/assets/circle-32.ico');
    game.load.image('red-circle', '/static/assets/circle-32.gif');
}

var protagonist;
var enemies;
var cursors;

function create() {
    // Some sort of necessary physics engine
    game.physics.startSystem(Phaser.Physics.ARCADE);

    // Protagonist creation
    initial_player_data = initial_data.player_data;
    protagonist = game.add.sprite(initial_player_data.x, initial_player_data.y, 'blue-circle');
    protagonist.name = username;
    game.physics.arcade.enable(protagonist);
    protagonist.body.collideWorldBounds = true;

    // I/O creation
    cursors = game.input.keyboard.createCursorKeys();

    // Other player data structure
    enemies = game.add.group();
    enemies.enableBody = true;

    var playerlist = initial_data.enemy_data.playerlist;
    for(var enemy_username in playerlist){
        if(enemy_username == username){
            continue;
        }
        if(playerlist.hasOwnProperty(enemy_username)){
            console.log(playerlist[enemy_username]);
            // var enemy = enemies.create(playerlist[enemy_username].x, playerlist[enemy_username].y, 'red-circle');
            // enemy.name = playerlist[enemy_username].username;
        }
    }
}

function update() {
    game.physics.arcade.collide(protagonist, enemies);

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

    socket.emit('LOCATION_UPDATE', {
        'username': username,
        'x': protagonist.x,
        'y': protagonist.y
    });
}

function getEnemyByName(username){
    enemies.forEach(function(enemy){
        if(enemy.name == username){
            return enemy;
        }
    });
}

socket.on('PLAYER_ADDED', function(player){
    enemy = enemies.create(player.x, player.y, 'red-circle');
    enemy.name = player.username;
});

socket.on('PLAYER_REMOVED', function(username){
    enemy = getEnemyByName(username);
    enemies.remove(enemy);
});

socket.on('GAME_UPDATE', function(message){
    if(message.username != username){
        return;
    }
    var payload = JSON.parse(message.payload);
    var playerlist = payload.playerlist;

    enemies.forEach(function(enemy){
        enemy.x = playerlist[enemy.name].x;
        enemy.y = playerlist[enemy.name].y;
    }, this);
});

$(window).unload(function(){
    socket.emit('GAME_CLOSE', {'username': username});
});
