import blocks
import hashlib

def most_recent():
    block = blocks.most_recent_block()
    blockNum = blocks.number(block)
    nonce = blocks.nonce(block)
    merkleRoot = blocks.merkle_root(block)
    hashValue = "".join([nonce, merkleRoot]).encode()
    randomStr = hashlib.sha224(hashValue).hexdigest()
    print("The random string for block %s is: %s" % (blockNum, randomStr))

def random_number_block(nonce, merkleRoot):
    print("hello")
    # do random number generation

def random_number_blocks(range):
    url = blockUrl + str(num)
