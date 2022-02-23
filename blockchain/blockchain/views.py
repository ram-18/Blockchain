from django.http import JsonResponse
import datetime
import hashlib
import json

class Blockchain:
    
    def __init__(self):
        self.chain = []
        self.create_block(nonce = 1, previous_hash = '0')
    
    def create_block(self, nonce, previous_hash):
        index = len(self.chain) + 1
        block = {
            'index': index,
            'timestamp': str(datetime.datetime.now()),
            'nonce': nonce,
            'previous_hash': previous_hash,
        }
        self.chain.append(block)
        return block
    
    def get_last_block(self):
        return  self.chain[-1]

    def proof_of_work(self, previous_nonce):
        new_nonce = 1
        check_nonce = False

        while not check_nonce:
            hash_operation = hashlib.sha256(str(new_nonce**2 - previous_nonce**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_nonce = True
            
            else:
                new_nonce += 1
        
        return new_nonce
    
    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys = True).encode()
        return hashlib.sha256(encoded_block).hexdigest()
    
    def is_chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1

        while block_index < len(chain):
            block = chain[block_index]

            if block['previous_hash'] != self.hash(previous_block):
                return False
            
            previous_nonce = previous_block['nonce']
            current_nonce = block['nonce']
            hash_operation = hashlib.sha256(str(current_nonce**2 - previous_nonce**2).encode()).hexdigest()
            
            if hash_operation[:4] != '0000':
                return False
            
            previous_block = block
            block_index += 1
        
        return True


blockchain = Blockchain()

def get_chain(request):
    if request.method == "GET":
        response = {
            'chain': blockchain.chain,
            'length': len(blockchain.chain),
        }
    return JsonResponse(response)

def mine_block(request):

    if request.method == "GET":
        previous_block = blockchain.get_last_block()
        previous_nonce = previous_block['nonce']
        new_nonce = blockchain.proof_of_work(previous_nonce)
        previous_hash = blockchain.hash(previous_block)
        block = blockchain.create_block(new_nonce, previous_hash)
        response = {
            'message': 'Block is mined',
            'block': block,
        }

    return JsonResponse(response)

def is_chain_valid(request):
    
    if request.method == "GET":
        is_valid = blockchain.is_chain_valid(blockchain.chain)
        
        if is_valid:
            response = {
                'message': 'blockchain is valid',
            }
        
        else:
            response = {
                'message': 'blockchain is invalid',
            }
    
    return JsonResponse(response)

def temper_blockchain(request):
    
    if request.method == "GET":
        
        l = len(blockchain.chain)
        print(l)
        if(l > 0):
            blockchain.chain[l-2]['nonce'] -= 34
            x = blockchain.chain[l-2]
        else:
            blockchain.chain[l-1]['nonce'] -= 34
            x = blockchain.chain[l-1]
        
    
    return JsonResponse(x)
