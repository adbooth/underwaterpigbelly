var username;
function getusername(delivered_username){
    username = delivered_username;
}
function username_request(callback){
    $.ajax({
        type: 'POST',
        success: callback
    });
}
username_request(getusername);
namespace = username;

var thisURL = location.protocol + '//' + document.domain + (location.port ? ':' + location.port : '');
var socketNamespace = thisURL + '/' + namespace;

// Create socket for data transfer
var socket = io.connect(socketNamespace);
