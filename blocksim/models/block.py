import time
from datetime import datetime
from blocksim.utils import keccak_256, encode_hex


class BlockHeader:
    """ Defines a basic BlockHeader model.

    In this first version of the simulator we do not simulate transactions merkle trees.

    :param str prevhash: the hash of the previous block
    :param str xorhash: the xor of the current block hash and the previous xorhash 
    :param int number: the number of ancestors of this block (0 for the genesis block)
    :param int timestamp: a UNIX timestamp
    :param str coinbase: coinbase address of the block miner, in this simulation we include the node address
    :param int difficulty: the blocks difficulty
    :param str nonce: a nonce constituting a Proof-of-Work
    """

    def __init__(self,
                 prevhash=encode_hex(b'\x00' * 32),
                 xorhash=encode_hex(b'\x00' * 32),
                 #xorhash,
                 number=0,
                 timestamp=int(time.time()),
                 coinbase=encode_hex(b'\x00' * 20),
                 difficulty=100000,
                 nonce=''):
        self.prevhash = prevhash
        self.xorhash = xorhash
        self.number = number
        self.timestamp = timestamp
        self.coinbase = coinbase
        self.difficulty = difficulty
        self.nonce = nonce

    @property
    def hash(self):
        """The block header hash"""
        k = encode_hex(keccak_256(str(self).encode('utf-8')))
        #self.xorhash = str(hex(int(self.xorhash[2:],16) ^ int(k[2:], 16)))
        return k
    # @property
    # def xorhash(self):
    #     if self.number == 0 or self.number==1:
    #         return encode_hex(b'\x00' * 32)
    #     #print('\n\t'+'--------------------------------------------------------------'+str(hex(int(self.prevhash.xorhash[2:],16) ^ int(self.prevhash[2:], 16)))+'\n\n')
    #     return str(hex(int(self.xorhash[2:],16) ^ int(self.prevhash[2:], 16)))

    def __repr__(self):
        """Returns a unambiguous representation of the block header"""
        return f'<{self.__class__.__name__}(#{self.number} {self.hash})>'

    def __str__(self):
        """Returns a readable representation of the block"""
        timestamp = datetime.utcfromtimestamp(
            self.timestamp).strftime('%m-%d %H:%M:%S')
        return f'<{self.__class__.__name__}(#{self.number} prevhash:{self.prevhash[:8]} xorhash:{self.xorhash[:8]} timestamp:{timestamp} coinbase:{self.coinbase} difficulty:{self.difficulty})>'

    def __eq__(self, other):
        """Two blocks are equal iff they have the same hash."""
        return isinstance(other, self.__class__) and self.hash == other.hash

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return self.hash
    # def __xorhash__(self):
    #     return self.xorhash


class Block:
    """ Defines the Block model.

    :param header: the block header
    :param transactions: a list of transactions
    """

    def __init__(self, header: BlockHeader, transactions=None):
        self.header = header
        self.transactions = transactions

    @property
    def transaction_count(self):
        return len(self.transactions)
