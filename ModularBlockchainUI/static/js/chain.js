// chain.js
$(document).ready(function() {
    $.get('/chain', function(data) {
        let chain = data.chain;
        chain.forEach(block => {
            $('#chainTable tbody').append(`
                <tr>
                    <td>${block.index}</td>
                    <td>${new Date(block.timestamp * 1000).toLocaleString()}</td>
                    
                    <td>${block.previous_hash}</td>
                    <td>${block.proof}</td>
                </tr>
            `);
        });
    });
});
