import blocks
from hashlib import md5
import hmac

KEY = b'RANDOM_KEY'

def most_recent():
    block = blocks.most_recent_block()
    blockNum, randomStr = random_str(block)
    print("The random string for block %s is: %s" % (blockNum, randomStr))

def specfic_block(num):
    block = blocks.block(num)
    blockNum, randomStr = random_str(block)
    print("The random string for block %s is: %s" % (blockNum, randomStr))

def multiple_blocks(range):
    multBlocks = blocks.recent_blocks(range)
    nonce = ""
    merkleRoot = ""
    for block in multBlocks:
        nonce = nonce.join(blocks.merkle_root(block))
        merkleRoot = merkleRoot.join(blocks.merkle_root(block))
    hashValue = "".join([nonce, merkleRoot]).encode()
    randomStr = hmac.new(KEY, hashValue, md5).hexdigest()
    #randomStr = hashlib.sha224(hashValue).hexdigest()
    print(randomStr)

def random_str(block):
    blockNum = blocks.number(block)
    nonce = blocks.nonce(block)
    merkleRoot = blocks.merkle_root(block)
    hashValue = "".join([nonce, merkleRoot]).encode()
    #randomStr = hashlib.sha224(hashValue).hexdigest()
    randomStr = hmac.new(KEY, hashValue, md5).hexdigest()
    return blockNum, randomStr

def random_number_blocks(range):
    url = blockUrl + str(num)
