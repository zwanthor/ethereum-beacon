import hashlib

def verify_random_num(num, verifyStr):
    block = blocks.block(num)
    nonce = blocks.nonce(block)
    merkleRoot = blocks.merkle_root(block)
    hashValue = "".join([nonce, merkleRoot]).encode()
    randomStr = hashlib.sha224(hashValue).hexdigest()
    if randomStr == verifyStr:
        print("The string matches")
    else:
        print("The string does not match")
