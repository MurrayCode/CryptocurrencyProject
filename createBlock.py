import hashlib
import time

class Create_Block:
    def __init__(self, index, new_num, last_hash, data, timestamp=None):
        self.index = index #keep track of position of the block within chain
        self.new_num = new_num #new block number 
        self.last_hash = last_hash #hash of previous block within the chain
        self.data = data #records all transactions
        self.timestamp = timestamp or time.time() #timestamp transaction
    
    @property #Hashing the Block
    def hash_block(self):
        block = "{}{}{}{}{}".format(self.index, self.new_num, self.last_hash, self.data, self.timestamp)
        return hashlib.sha256(block.encode()).hexdigest()

    def __repr__(self):
        return "{} - {} - {} - {} - {}".format(self.index, self.new_num, self.last_hash, self.data, self.timestamp)