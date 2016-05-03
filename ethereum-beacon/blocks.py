import requests
import json

blockCountUrl = "https://etherchain.org/api/blocks/count"
blockUrl = "https://etherchain.org/api/block/"
blocksUrl = "https://etherchain.org/api/blocks/"

# returns json for most recently mined block
def most_recent_block():
    blockNum = recent_block_num()
    return block(blockNum)

# return the number of the most recently mined block
def recent_block_num():
    response = requests.get(blockCountUrl)
    jsonData = json.loads(response.content.decode('utf-8'))
    blockNum = jsonData["data"][0]["count"]
    return blockNum

# return block specified by its number
def block(num):
    url = blockUrl + str(num)
    response = requests.get(url)
    jsonData = json.loads(response.content.decode('utf-8'))
    block = jsonData["data"][0]
    return block

# return the most recent blocks in a range
def recent_blocks(range):
    data = []
    blocks = []
    recBlockNum = recent_block_num()
    offset = recent_block_num()-range
    url = blocksUrl + "%s/%s" % (str(offset), str(range))
    response = requests.get(url)
    for block in response:
        jsonData = json.loads(response.content.decode('utf-8'))
        data.append(jsonData)
    for block in blocks[0]["data"]:
        blocks.append(block)
    return blocks

#take in block representation as json and returns its number
def number(block):
    return block["number"]

#take in block representation as json and returns its nonce
def nonce(block):
    return block["nonce"]

#take in block representation as json and returns its merkle root
def merkle_root(block):
    return block["root"]

#take in block representation as json and returns its coinbase
def coinbase(block):
    return block["coinbase"]

#take in block representation as json and returns its txHash
def txHash(block):
    return block["txHash"]
