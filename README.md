# Blockchain Team Selection Task
Block Structure:
Every block in the chain contains an index — for showing its position in the chain starting from 0, data — the actual data stored in the block, nonce — this is just a number we assign to help secure the block, timestamp — to know when each block is created, hash — a unique identifier for the block (same as a virtual fingerprint), and hash of the previous block — to link all the blocks in the chain.

Validity Testing of Chain:
To make sure the blockchain isn't tampered with, we check if each block’s recorded previous hash actually matches the hash of the block before it. If the check fails, it means the block has been modified, because the hash of the block changes even when something minor is changed in the block.

Proof of Work Approach:
To ensure security and integrity, each block is mined using a simple Proof-of-Work mechanism. The goal is to find a nonce such that the hash of the block starts with a certain number of zeros (e.g. "00" for difficulty 2). This is done by trying different nonce values until the condition is met.
This process requires computational effort, like in real-world blockchain networks such as Bitcoin, making it difficult to tamper with the chain. The more zeros required at the start of the hash, the harder the block is to mine.
The function mine_block handles this by brute-forcing a valid nonce.
