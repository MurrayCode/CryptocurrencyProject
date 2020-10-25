import hashlib
import time
from createBlock import *

class Create_Chain():
    def __init__(self):
        self.blockchain = [] #store blocks
        self.transaction_data = []  #store all transactions
        self.nodes = set()
        self.build_initial() #build the first block

    def build_initial(self):
        self.build_block(new_num = 0, last_hash = 0)

    def build_block(self, new_num, last_hash):
        block = Create_Block(index = len(self.blockchain),
            new_num = new_num, last_hash = last_hash,
            data = self.transaction_data)
        self.transaction_data = []
        self.blockchain.append(block)
        return block


    def new_information(self, sender, receiver, quantity):
        self.transaction_data.append({
            'sender': sender,
            'recipient': receiver,
            'quantity': quantity
        })
        return True

    @property
    def most_recent_block(self):
        return self.blockchain[-1]

    @staticmethod
    def proof_of_work(last_proof):
        proof_no = 0
        while Create_Chain.checking_proof(proof_no, last_proof) is False:
            proof_no += 1
        return proof_no


    @staticmethod
    def checking_proof(last_proof, proof):
        answer = f'{last_proof}{proof}'.encode()
        hash_answer = hashlib.sha256(answer).hexdigest()
        return hash_answer[:4] == "0000"

    @staticmethod
    def check_block_chain(block, last_block):
        if last_block.index + 1 != block.index:
            return False
        elif last_block.hash_block != block.last_hash:
            return False
        elif not Create_Chain.checking_proof(block.last_num, last_block.last_num):
            return False
        elif block.time <= last_block.time:
            return False
        return True

    def block_mining(self, details_miner):

        self.new_data(
            sender="0",  
            receiver=details_miner,
            quantity=
            1,  
        )
        last_block = self.latest_block
        last_proof_no = last_block.proof_no
        proof_no = self.proof_of_work(last_proof_no)
        last_hash = last_block.calculate_hash
        block = self.construct_block(proof_no, last_hash)
        return vars(block)

    def create_node(self, address):
        self.nodes.add(address)
        return True

    @staticmethod
    def obtain_block_object(block_data):
        #obtains block object from the block data
        return Create_Block(
            block_data['index'],
            block_data['new_num'],
            block_data['last_hash'],
            block_data['data'],
            timestamp=block_data['timestamp'])