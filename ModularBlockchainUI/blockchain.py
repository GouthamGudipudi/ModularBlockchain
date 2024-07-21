import hashlib
import json
import time

class Block:
    def __init__(self, index, proof, previous_hash, data):
        self.index = index
        self.proof = proof
        self.previous_hash = previous_hash
        self.timestamp = time.time()
        self.data = data

    def to_dict(self):
        return {
            'index': self.index,
            'proof': self.proof,
            'previous_hash': self.previous_hash,
            'timestamp': self.timestamp,
            'data': self.data
        }

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_block(previous_hash='0', proof=100)

    def create_block(self, proof, previous_hash):
        block = Block(
            index=len(self.chain) + 1,
            proof=proof,
            previous_hash=previous_hash,
            data=[]
        )
        self.chain.append(block)
        return block

    def get_previous_block(self):
        return self.chain[-1]

    def get_chain(self):
        return [block.to_dict() for block in self.chain]

    def hash_block(self, block):
        encoded_block = json.dumps(block.to_dict(), sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

class Consensus:
    @staticmethod
    def proof_of_work(last_proof):
        proof = 0
        while not Consensus.is_valid_proof(last_proof, proof):
            proof += 1
        return proof

    @staticmethod
    def is_valid_proof(last_proof, proof):
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

class SmartContract:
    def __init__(self, blockchain):
        self.blockchain = blockchain

    def create_transaction(self, sender, recipient, amount):
        previous_block = self.blockchain.get_previous_block()
        transaction = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        }
        previous_block.data.append(transaction)
        return previous_block.index
