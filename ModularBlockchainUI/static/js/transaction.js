// transaction.js
$(document).ready(function() {
    $('#transactionForm').submit(function(event) {
        event.preventDefault();
        let sender = $('#sender').val();
        let recipient = $('#recipient').val();
        let amount = $('#amount').val();

        $.ajax({
            url: '/transactions/new',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({
                sender: sender,
                recipient: recipient,
                amount: amount
            }),
            success: function(data) {
                $('#transactionResult').html(`
                    <div class="alert alert-success">
                        ${data.message}
                    </div>
                `);
                $('#transactionForm')[0].reset();
            },
            error: function(error) {
                $('#transactionResult').html(`
                    <div class="alert alert-danger">
                        Error: ${error.responseJSON.error}
                    </div>
                `);
            }
        });
    });
});
