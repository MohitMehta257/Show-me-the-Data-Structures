import hashlib
import datetime as dt


class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()
        
    def calc_hash(self):
      sha = hashlib.sha256()

      hash_str = "We are going to encode this string of data!".encode('utf-8')

      sha.update(hash_str)

      return sha.hexdigest()
    

def get_time():
    time=dt.datetime.now()
    return time
    
class LinkedList:
        def __init__(self):
            self.head=None
            self.next=None
        def append(self,timestamp,data):
            if self.head is None:
                self.head = Block(timestamp,data,0)
                return
            else:
                value=self.next
                self.next = Block(timestamp, data, value)
                

block0 = Block(get_time(), "Books Name", 0)
block1 = Block(get_time(), "Important Info", block0)
block2 = Block(get_time(), "Corona", block1)

print(block0.data)
print(block2.hash)
print(block0.timestamp)
print(block1.previous_hash.data)
print(block2.data)
