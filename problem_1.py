
class LRU_Cache(object):

    def __init__(self, capacity=5):
        # Initialize class variables
        self.dict={}
        self.capacity=capacity
        self.list=[]

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key in self.dict.keys(): 
            return key
        else:
            return -1
        
      

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if key in self.dict.keys():
            return None
        if key not in self.dict.keys():
            
            
            if len(self.dict)>=5:
                d_value=self.list[0]
                del self.list[0]
                del self.dict[d_value]
                self.list.append(key)
                self.dict[key]=value
            else:
                self.list.append(key)
                self.dict[key]=value
                
                
                

                
            
our_cache=LRU_Cache(5)
our_cache.set(7, 1)
our_cache.set(2, 2)
our_cache.set(6, 2)
our_cache.set(5, 2)
our_cache.set(9, 2)


print(our_cache.get(1))       # returns -1
print(our_cache.get(2))       # returns 2
