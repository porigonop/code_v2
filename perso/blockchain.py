import hashlib
import struct
class Transaction:
    amount = 0
    source = ''
    destination = ''
    def __init__(self, amount, source, destination):
        self.amount = amount
        self.source = source
        self.destination = destination

    def __repr__(self):
        return  str(self.amount)\
               + self.source\
               + self.destination

class Block:
    bloc_number = 0
    previous = ''
    transactions = []
    padding = ''

    def __repr__(self):
        return str(self.bloc_number)\
               + str(self.previous)\
               + str(' '.join([str(t) for t in self.transactions]))\
               + self.padding
    def hash(self):
        return hashlib.md5(str(self).encode('utf-8')).digest()



class Blockchain:
    chain = []
    transactions = []
    last_block = None
    number_of_0 = 2

    def new_block(self):
        '''
        cette methode creera un nouveau bloc dans la blockchain, copiera les transactions recentes dans ce nouveau bloc et effacera l’ensemble des transactions.
        '''
        self.last_block = Block()
        self.last_block.bloc_number = (self.chain[-1].bloc_number + 1) if self.chain else 0
        self.last_block.transactions = self.transactions
        if self.chain:
            self.last_block.previous = self.chain[-1].hash()
        self.transactions = []

    def valid_proof(self, block):
        '''
        ce code verifiera que le bloc soumis pour être ajoute à la blockchain resout le problème.:
        '''
        val = int.from_bytes(block.hash()[-self.number_of_0:], byteorder='big')
        # print(block.hash()[-self.number_of_0:], val)
        if val != 0:
            return False
        self.chain.append(block)
        return True

    def new_transaction(self, transaction):
        '''
        ce code va ajouter une nouvelle transaction à la liste des transactions.
        '''
        self.transactions.append(transaction)
        return True

if __name__ == '__main__':
    import random

    blockchain = Blockchain()

    blockchain.new_transaction(Transaction(100, 'antoine', 'virgile'))
    blockchain.new_block()
    



    block = blockchain.last_block
    print(blockchain.number_of_0)
    choice = 'qwertyuiopasdfghjklzxcvbnm'
    len_choice = len(choice)
    while True:
        block.padding = ''.join([choice[int(random.random()*len_choice)] for _ in range(10)])
        if blockchain.valid_proof(block):
            break


    blockchain.new_transaction(Transaction(100, 'antoine', 'virgile'))
    blockchain.new_transaction(Transaction(100, 'antoine', 'virgile'))
    blockchain.new_block()

    block = blockchain.last_block
    print(blockchain.number_of_0)
    while True:
        block.padding = ''.join([choice[int(random.random()*len_choice)] for _ in range(10)])
        # print(block)
        if blockchain.valid_proof(block):
            break


    blockchain.new_transaction(Transaction(100, 'antoine', 'virgile'))
    blockchain.new_transaction(Transaction(100, 'antoine', 'virgile'))
    blockchain.new_block()


    block = blockchain.last_block
    print(blockchain.number_of_0)
    while True:
        block.padding = ''.join([choice[int(random.random()*len_choice)] for _ in range(10)])
        # print(block)
        if blockchain.valid_proof(block):
            break
    print(blockchain.chain)
