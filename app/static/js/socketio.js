const socket = io.connect('http://localhost:5000');

socket.on('progress_update', function(data) {
    console.log('Progress:', data.progress);
});

function startProcessing() {
    socket.emit('start_processing', {data: 'start'});
}
