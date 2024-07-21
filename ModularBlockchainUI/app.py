from flask import Flask, jsonify, request, render_template
from blockchain import Blockchain, Consensus, SmartContract

app = Flask(__name__)
blockchain = Blockchain()
smart_contract = SmartContract(blockchain)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mine', methods=['POST'])
def mine():
    try:
        last_block = blockchain.get_previous_block()
        last_proof = last_block.proof if last_block else 100
        proof = Consensus.proof_of_work(last_proof)
        previous_hash = blockchain.hash_block(last_block)

        block = blockchain.create_block(proof, previous_hash)
        response = {
            'message': 'New Block Forged',
            'index': block.index,
            'data': block.data,
            'proof': block.proof,
            'previous_hash': block.previous_hash,
        }
        return jsonify(response), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/mine.html', methods=['GET'])
def mine_page():
    return render_template('mine.html')

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    try:
        values = request.get_json()

        required = ['sender', 'recipient', 'amount']
        if not all(k in values for k in required):
            return 'Missing values', 400

        index = smart_contract.create_transaction(values['sender'], values['recipient'], values['amount'])
        response = {'message': f'Transaction will be added to Block {index}'}
        return jsonify(response), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/transaction.html', methods=['GET'])
def transaction_page():
    return render_template('transaction.html')

@app.route('/chain', methods=['GET'])
def view_chain():
    try:
        chain = blockchain.get_chain()
        response = {
            'chain': chain,
            'length': len(chain),
        }
        return jsonify(response), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/chain.html', methods=['GET'])
def chain_page():
    return render_template('chain.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
