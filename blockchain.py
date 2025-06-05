import hashlib
import time
class Block:
    def __init__(self,blockdata,previousblock,nonce):
        self.blockdata=blockdata
        self.nonce=nonce
        self.timestamp=time.time()
        if previousblock==None: #If this is first block
            self.index=0
            self.previous_block_hash=""
        else:  self.index=previousblock.index+1
        if previousblock!=None:
            self.previous_block_hash=previousblock.hash
        self.hash=hashlib.sha256((str(self.index)+str(self.timestamp)+str(blockdata)+str(self.previous_block_hash)+str(nonce)).encode()).hexdigest()
    def __str__(self):  # For printing the block
        return f"Index:{self.index}\nBlockdata:{self.blockdata}\nTimestamp:{self.timestamp}\nhash:{self.hash}\nPrevious_block_hash={self.previous_block_hash}\n"
    
class Blockchain:
    def __init__(self,genesis_block_data,nonce):
        self.chain=[]
        genesis_block=Block(genesis_block_data,None,nonce)
        self.chain.append(genesis_block)
    def add_block(self,data,nonce):
        new=Block(data,self.chain[-1],nonce)
        self.chain.append(new)
    def isvalid(self):
        for i in range(1,len(self.chain)):
            this=self.chain[i]
            prev=self.chain[i-1]
             # Check if the stored hash matches the recalculated hash
            if this.hash!=hashlib.sha256((str(this.index)+str(this.timestamp)+str(this.blockdata)+str(this.previous_block_hash)+str(this.nonce)).encode()).hexdigest():
                print(f"Hash of {i+1}'th block doesn't match")

                return False
            if prev.hash!=this.previous_block_hash:   # Check if current block's previous hash matches previous block's hash
                print("The Blockchain is tampered!")
                return False
        print("The Blockchain is valid.")
        return True


for i in range(1,1000):
    data="The block data"
    req_block=Block(data,None,i)
    if req_block.hash.startswith("00"):
        print("required block is")
        print(req_block)
        break
def mine_block(data, previous_block, difficulty=2):  # Finds nonce so block hash starts with leading zeros
    prefix = '0' * difficulty
    for nonce in range(1, 1000000):  
        block = Block(data, previous_block, nonce)
        if block.hash.startswith(prefix):
            print("Required block is:")
            print(block)
            return block
    print("Mining failed, couldn't find block.")
    return None
# Simple mining demonstration for difficuly=2
A = Block("Genesis Block", None, 0)
print("Genesis Block:")
print(A)

mined_block = mine_block("Test block data", A)
























