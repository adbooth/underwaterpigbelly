Crafty.init(500, 350, document.getElementById('game'));

Crafty.e('2D, DOM, Color, Fourway, Gravity')
    .attr({x: 0, y: 0, w: 100, h: 100})
    .color('#F00')
    .fourway(5)
    .gravity('Floor');

Crafty.e('Floor, 2D, DOM, Color')
    .attr({x: 0, y: 350, w: 500, h: -20})
    .color('#F01')
