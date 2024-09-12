$(document).ready(function() {
    // Initialize SocketIO connection
    var socket = io.connect('http://' + document.domain + ':' + location.port);

    // Handle real-time updates
    socket.on('parcel_status', function(data) {
        $('#status-display').text(data.status);
    });

    // Track live button click event
    $('#track-live-button').click(function() {
        socket.emit('track_parcel', { data: 'track' });
    });
});


