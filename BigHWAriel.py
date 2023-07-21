import time 
import random
import pytest 
from BitHash import *
import pytest 

# I hereby certify that this program is solely the result of my own work and is in
# compliance with the Academic Integrity policy of the course syllabus and the 
# academic integrity policy of the CS department



# This class creates a Bucket with a Key and Data Pair, which will be inputed 
# into the Cuckoo Hash
class Bucket(object): 
    
    def __init__(self, k, d):
        self.__key= k 
        self.__data=d 
        
    # Getter for the Key 
    def getKey(self): return self.__key 
    
    # Getter for the Data
    def getData(self): return self.__data 
        
        
class CuckooHash(object): 
    
    
    def __init__(self, size): 
        # A Cuckoo Hash is initialized with a size. 
        # Size is the amount of memory in the Cuckoo Hash. 
        self.__size= size 
        
        # A Cuckoo Hash has two Arrays, both are initially filled with Nones.
        self.__hashOne = [None] * size
        self.__hashTwo = [None] * size 
        
        # totalNumKeys is the amount of keys inserted into the Cuckoo Hash
        self.__totalNumKeys = 0 
        
    # length returns the total number of keys that have been inserted into the array. 
    def length(self): return self.__totalNumKeys 
    
    # Getter for the size of the array
    def getSize(self): return self.__size
    
    
    # Insert takes in 4 parameters: 
    
    # k is the key 
    # d is the data 
    
    # shouldAdd is a boolean that represents whether or not the 
    # total number of keys in the Cuckoo Hash should be incremented. 
    # because insertIntoTwo calls normal insert, shouldAdd ensures that the 
    # Cuckoo Hash will only increment total number of keys when a new key is 
    # being inserted 
    
    # times represents the number of times that insertIntoTwo had to call insert. 
    # if times is too high of a number, the code will reset the bit hash and set 
    # times = 0. 
    def insert(self, k, d, shouldAdd=True, times=0): 
        
        # if it is a new key, increment totalNumKeys
        if shouldAdd==True: self.__totalNumKeys+=1 
        
        # Here shouldRebuild is called. 
        # shouldRebuild both grows if necessary and if it returns true 
        # that means that it was necessary to ResetBitHash() and so 
        # reset times to be 0. 
        if self.shouldRebuild(times)==True: times=0
        
        # hashVal represents the place in the first hash table that a bucket 
        # should be inserted into. 
        hashVal = BitHash(k) % len(self.__hashOne) 
        
        # if hashOne is empty at hashVal
        if not self.__hashOne[hashVal]: 
            # create a new Bucket Object
            b= Bucket(k, d) 
            
            # insert the bucket into Hash One at hashVal position
            self.__hashOne[hashVal]=b 
      
        # if hashOne is filled at hashVal
        elif self.__hashOne[hashVal]:
            
            # save the bucket that is already in HashOne
            bucket= self.__hashOne[hashVal] 
            
            # save the key and data 
            key=bucket.getKey() 
            data=bucket.getData() 
            
            # call insert into two to insert the key and data pair, which was 
            # origionally in hashOne, into the second hash table. 
            
            self.insertIntoTwo(key,data, times) 
            
            # make the position in hashOne at hashVal be a newly created bucket 
            # with the new k and d pair. 
            self.__hashOne[hashVal]= Bucket(k,d) 
    
    
    # insertIntoTwo takes as parameter the key and data pair that was origionally 
    # in HashOne, but was evicted. 
    
    # insertIntoTwo also takes in times as a paremter, because insertIntoTwo will
    # increment times every time it needs to call insert. 
    
    
    def insertIntoTwo(self, k, d, times): 
        
        # hashVal represents the position in hashTwo using a different hash function 
        # than the one used for insert into hashOne. 
        
        hashVal = BitHash(k, 2) % len(self.__hashTwo)
        
        # if hashTwo is empty at hashVal
        if not self.__hashTwo[hashVal]: 
            # create a new Bucket Object
            b = Bucket(k, d)  
            # insert the bucket into Hash Two at hashVal position
            self.__hashTwo[hashVal]= b
        
        # if hashTwo is filled at hashVal 
        elif self.__hashTwo[hashVal]:
            
            # save the bucket that is in hashTwo
            bucket= self.__hashTwo[hashVal] 
            
            # get the key and data in that bucket.
            key=bucket.getKey() 
            data=bucket.getData() 
            
            # call insert, evicting what was in hashTwo and trying to insert it in 
            # hashOne
            
            # use the False parameter to indicate that totalNumKeys 
            # should not be incremented
            
            # increment times, this will make sure that a infinite loop does not occur. 
            self.insert(key,data,False, times+1)  
            
            # create a new bucket with the k,d and insert it into hashTwo.
            
            self.__hashTwo[hashVal]=Bucket(k, d)  
            
    # shouldRebuild checks to make sure that the hash isn't too full 
    # in addition, it checks to make sure that an infinite loop was not detected.
    def shouldRebuild(self, times): 
        
        # filled amount represents the ratio of keys to the size of the Hash Array
        filledAmount= self.__totalNumKeys / self.__size     
        
        # if filled amount is greator then .5 then the hash should grow. 
        if filledAmount>=.5: self.grow() 
        
        # if times is greator then 50 then an infinite loop has been detected
        if times>50: 
            # Reset the bit hash will use two different hash functions when hashing 
            
            ResetBitHash() 
            
            # because the hash functions have been reset, all of the key/data pairs 
            # need to be re-hashed and re-inputed. 
            
            # save both old hash tables
            oldOne= self.__hashOne 
            oldTwo= self.__hashTwo 
            
            # save the totalNumKeys
            oldNumKeys=self.__totalNumKeys
            
            # create two new hash tables
            newOne= [None] * self.__size 
            newTwo= [None] * self.__size 
            
            # make self's hashTables be the two newly created hashTables
            self.__hashOne = newOne 
            self.__hashTwo = newTwo
           
            # loop through the buckets in oldOne
            for bucket in oldOne: 
                # if a bucket is there
                if bucket: 
                    # insert into the newly created self's hashTable
                    self.insert(bucket.getKey(), bucket.getData(), False) 
                    
            # loop through the buckets in oldTwo       
            for bucketTwo in oldTwo: 
                # if there is a bucket 
                if bucketTwo:
                    # insert it into the newly created self's hashTable
                    self.insert(bucketTwo.getKey(), bucketTwo.getData(), False)
            
            # make self's numKeys = oldNumKeys    
            self.__totalNumKeys=oldNumKeys             
            
            # if the BitHash was rebuilt, then return true so that times could be 
            # reset to zero.
            return True 
       
    def grow(self): 
        
        # grow the hash table's size by two 
        self.__size= self.__size * 2
        
        # save both old hash tables
        oldOne= self.__hashOne 
        oldTwo= self.__hashTwo 
        
        # save the totalNumKeys
        oldNumKeys=self.__totalNumKeys
        
        # create two new hash tables
        newOne= [None] * self.__size 
        newTwo= [None] * self.__size 
        
        # make self's hashTables be the two newly created hashTables
        self.__hashOne = newOne 
        self.__hashTwo = newTwo
       
        # loop through the buckets in oldOne
        for bucket in oldOne: 
            # if there is a bucket 
            if bucket: 
                # insert it into the newly created self's hashTable
                self.insert(bucket.getKey(), bucket.getData(), False) 
                
        # loop through the buckets in oldTwo        
        for bucketTwo in oldTwo: 
            # if there is a bucket
            if bucketTwo:
                # insert it into the newly created self's hashTable
                self.insert(bucketTwo.getKey(), bucketTwo.getData(), False)
                
        # make self's numKeys = oldNumKeys        
        self.__totalNumKeys=oldNumKeys      
    
    # search will return the data that corresponds to key in the CuckooHash
    def search(self, k): 
        
        # the hashed value that k's data should be in hashOne
        hashVal= BitHash(k) % self.__size  
        # the hashed value that k's data should be in hashTwo
        hashValTwo=BitHash(k, 2) % self.__size 
        
        # These are the buckets that correspond to hashVal one and hashVal two
        bucketOne= self.__hashOne[hashVal] 
        bucketTwo= self.__hashTwo[hashValTwo] 
        
        # if the key is in hashOne, return the data 
        if  bucketOne and bucketOne.getKey()==k : return bucketOne.getData()
        
        # or if the key is in hashTwo, return the data
        elif bucketTwo and bucketTwo.getKey()==k: return bucketTwo.getData() 
        
        # if the key could not be found in either hashOne or hashTwo, 
        # return False, the key/data was not found in the Cuckoo Hash
        return False
    
    # delete will delete the bucket at k's hashValue in the CuckooHash
    def delete(self,k): 
        
        # the hashed value that k's data should be in hashOne
        hashVal= BitHash(k) % self.__size 
        
        # the hashed value that k's data should be in hashTwo
        hashValTwo=BitHash(k, 2) % self.__size 
        
        # These are the buckets that correspond to hashVal one and hashVal two
        bucketOne= self.__hashOne[hashVal] 
        bucketTwo= self.__hashTwo[hashValTwo] 
        
        # if the k was found at bucketOne
        if  bucketOne and bucketOne.getKey()==k: 
            # set it to None
            self.__hashOne[hashVal]=None 
            
            # decrement the totalNumKeys
            self.__totalNumKeys-=1
            
            # return True because the delete was successful
            return True 
        
        # if the k was found at bucketTwo
        elif bucketTwo and bucketTwo.getKey()==k: 
            
            # set it to None
            self.__hashTwo[hashValTwo]=None 
            
            # decrement the totalNumKeys
            self.__totalNumKeys-=1 
            
            # return True because the delete was successful
            return True 
        
        # return False, the key was not found in the Cuckoo Hash and therefore 
        # it could not be deleted. 
        return False       
    
    # This function is used in the pytests, it puts all the values in the Cuckoo Hash 
    # into an array. 
    def intoArray(self):
        
        inserts=[] 
        # loop through the buckets in hashOne
        for bucket in self.__hashOne: 
            # append every data and key into the array 
            if bucket: inserts.append((bucket.getData(), bucket.getKey())) 
        
        # loop through the buckets in hashTwo    
        for bucket in self.__hashTwo: 
            # append every data and key into the array
            if bucket: inserts.append((bucket.getData(), bucket.getKey())) 
            
        # returns the array of all the values in the CuckooHash   
        return inserts
                
       
def __main(): 
    pass
    
    
if __name__ == '__main__': __main() 


# this test inserts One Hundred Thousand Key, Data Pairs and checks the 
# length of the Cuckoo Hash to make sure that all of the Key, Data pairs were 
# inserted. 
def test_bigInsertLength(): 
    c=CuckooHash(1) 
    for i in range(100000): 
        c.insert(i,i) 
        
    assert c.length()==100000
    
# This test puts all of One Hundred Thousand Inserts into an Array 
# Then, it checks to make sure that the max and min are the correct numbers. 
def test_minMaxTestBigInsert(): 
    c=CuckooHash(1) 
    
    for i in range(100000): 
        c.insert(i,i) 
        
    array=c.intoArray() 
    assert max(array) == (99999, 99999)
    
    assert min(array) == (0, 0)  
    
# This test puts a smaller number (One Hundred) inserts into an Array 
# Then, it checks to make sure that the max and min are the correct numbers. 
def test_minMaxTestSmallInsert():
    c=CuckooHash(1) 
    
    for i in range(100): 
        c.insert(i,i) 
        
    array=c.intoArray() 
    
    assert max(array) == (99, 99)
    
    assert min(array) == (0, 0) 
    
# This test puts in 10 thousand inserts into the Cuckoo Hash 
# It then searches for them, and increments the count if 
# the data is not there. 

# Then it will search for 10,000 numbers that are not there. Make sure there 
# are not any false positives. 

def test_noFalsePositives(): 
    
    c=CuckooHash(1) 
    count=0
    
    for i in range(10000):   
        c.insert(i,i) 
        if c.search(i) != i: count+=1 
    # assert all of the inserts were found. count should be zero 
    assert count==0 
    
    
    countTwo=0 
    # These numbers were never inserted
    for d in range(20000, 30000): 
        if c.search(d)!=False: countTwo+=1 
    
    # assert that there are no false positives
    assert countTwo==0 
    
# This tests inserts  100,000 numbers, deletes and makes sure that 
# they could not be searched for after the delete. 

# In addition, that the len should be zero after the inserts. 
def test_delete(): 
    c=CuckooHash(1) 
    
    for i in range(100000):
        c.insert(i,i) 
        c.delete(i) 
        assert c.search(i)==False
        
    assert c.length()==0 
    
# This test inserts random data into the Cuckoo Hash. 
# It makes sure that they could be searched for and found. 

# Then = it deletes the number, and does another search. Making sure that 
# the number that should have been deleted was deleted. 
def test_tortureTest(): 
    
    c=CuckooHash(1) 
    
    for i in range(10000):
        rand= random.randint(0,100)
        c.insert(i,rand) 
        assert c.search(i) == rand 
        c.delete(i) 
        assert c.search(i) == False 
        
# This test makes sure that after all the inserts are done, items could still be 
# searched for. 
# The idea behind this test is to make sure that a infinite loop does not occur
# when the Cuckoo Hash is filled already before doing searches.       
def test_seperateForLoopsInsertBig(): 
    c=CuckooHash(1) 
    
    for i in range(100000): 
        c.insert(i,i)  
        
    for x in range(100000):
        assert c.search(x) == x 
    
# This test does 100 inserts and makes sure that the length is 100
def test_lengthSmall(): 
    
    c=CuckooHash(1) 
    for i in range(100): 
        c.insert(i,i) 
    assert c.length()==100 

pytest.main(["-v","-s", "BigHWAriel.py"])