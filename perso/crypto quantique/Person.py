import random
from Message import Message

class Person():
    def __init__(self, name):
        self.name = name
        self.message = None
        self.Qcode = None
    def create_message(self, message):
        self.message = Message(message)

    def send_message(self):
        return self.message.encode(1, 0.1)
    def receive_message(self, Qcode):
        self.Qcode = Qcode

    def decode_message(self):
        dec_msg = []
        for qbit in self.Qcode:
            if random.random()> 0.5:
                dec_msg.append(("z", qbit.measure("z")))
            else:
                dec_msg.append(("x", qbit.measure("x")))
        self.message = dec_msg
if __name__ == "__main__":
    A = Person("alice")
    A.create_message("a")
    msg = A.send_message()
    B = Person("bob")
    B.receive_message(msg)
    B.decode_message()
    print(B.message)