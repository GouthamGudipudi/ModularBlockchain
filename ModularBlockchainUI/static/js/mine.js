$(document).ready(function() {
    $('#mineButton').click(function() {
        $.post('/mine', function(data) {
            $('#mineResult').html(`
                <div class="alert alert-success">
                    <strong>${data.message}</strong><br>
                    Index: ${data.index}<br>
                    Data: ${data.data}<br>
                    Proof: ${data.proof}<br>
                    Previous Hash: ${data.previous_hash}
                </div>
            `);
        }).fail(function(xhr) {
            $('#mineResult').html(`
                <div class="alert alert-danger">
                    Error: ${xhr.responseJSON.error}
                </div>
            `);
        });
    });
});
