from createChain import *
from createBlock import *

if __name__ == '__main__':

    new_blockchain = Create_Chain()
   # print("Mining Smackeroonis")
   # print(new_blockchain.blockchain)

    last_block = new_blockchain.most_recent_block
    last_proof_no  = last_block.new_num
    proof_no = new_blockchain.proof_of_work(last_proof_no)

    new_blockchain.new_information(
        sender = "0",
        receiver = "Murray Stewart",
        quantity = 1,
    )
    last_hash = last_block.hash_block
    block = new_blockchain.build_block(proof_no, last_hash)

   #print("Mining Smackeroonis was Successful")
   # print(new_blockchain.blockchain)

   # print("Mining Smackeroonis")
    #print(new_blockchain.blockchain)

    last_block = new_blockchain.most_recent_block
    last_proof_no  = last_block.new_num
    proof_no = new_blockchain.proof_of_work(last_proof_no)

    new_blockchain.new_information(
        sender = "Murray Stewart",
        receiver = "Test Reciever",
        quantity = 1,
    )
    last_hash = last_block.hash_block
    block = new_blockchain.build_block(proof_no, last_hash)

    #print("Mining Smackeroonis was Successful")
    #print(new_blockchain.blockchain)

    #print("Mining Smackeroonis")
    #print(new_blockchain.blockchain)

    last_block = new_blockchain.most_recent_block
    last_proof_no  = last_block.new_num
    proof_no = new_blockchain.proof_of_work(last_proof_no)

    new_blockchain.new_information(
        sender = "test Reciever",
        receiver = "Test Reciever",
        quantity = 1,
    )
    last_hash = last_block.hash_block
    block = new_blockchain.build_block(proof_no, last_hash)

    print("Mining Smackeroonis was Successful")
    print(new_blockchain.blockchain)
