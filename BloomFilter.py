from BitHash import BitHash
from BitVector import BitVector

class BloomFilter(object):
    # Return the estimated number of bits needed in a Bloom 
    # Filter that will store numKeys keys, using numHashes 
    # hash functions, and that will have a
    # false positive rate of maxFalsePositive 
    
    def __bitsNeeded(self, numKeys, numHashes, maxFalsePositive):
    # phi is the proportion of bits still zero in B after inserting n keys
        phi= 1- (maxFalsePositive**(1/numHashes))
        
    # N = how long the bit vector should be
        N = numHashes/(1 - phi**(1/numKeys))
        return int(N)
    
    
    # Create a Bloom Filter that will store numKeys keys, using 
    # numHashes hash functions, and that will have a false positive 
    # rate of maxFalsePositive.

    def __init__(self, numKeys, numHashes, maxFalsePositive):
        # will need to use __bitsNeeded to figure out how big
        # of a BitVector will be needed
        
        self.__numKeys=numKeys 
        self.__numHashes=numHashes 
        self.__maxFalsePositive=maxFalsePositive
        # the number of bits set, this is not the same as the number of Keys.
        self.__setBits=0 
    
        self.__bloomF= BitVector(size = self.__bitsNeeded(numKeys, numHashes,maxFalsePositive))
        
    # insert the specified key into the Bloom Filter.
    # Doesn't return anything, since an insert into 
    # a Bloom Filter always succeeds!
   
    def insert(self, key):
        # loop through all of the hashes. 
        for i in range(1, self.__numHashes+1):                
            # set bit vector at hashed place to be a 1 (do this for all hash functions until numHashes  
            bucket = (BitHash(key, i) % len(self.__bloomF)) 
            # set this spot to a 1 
            if self.__bloomF[bucket]!=1:
                self.__bloomF[bucket]=1 
                # increment the number of bits 
                self.__setBits+=1 
           
                
    # Returns True if key MAY have been inserted into the Bloom filter. 
    # Returns False if key definitely hasn't been inserted into the BF.
   
    def find(self, key):
        # loop through the number of hash functions 
        for i in range(1, self.__numHashes+1):                      
            # if the bit inside the hashfunction-produced bucket in bloomfilter is not a 1 return false
            # The key is for sure not in the bloom filter 
            # Do this for every hash function 
            bucket=(BitHash(key,i) % len(self.__bloomF))
            if self.__bloomF[bucket]!=1: return False 
        # If all of the buckets have a 1, the key may be in the bloom filter 
        return True                    
       
    # Returns the PROJECTED current false positive rate based on the
    # ACTUAL current number of bits actually set in this Bloom Filter. 
     
    def falsePositiveRate(self): 
        # phi is the number of bits still zero over the total amount of bits 
        phi=(len(self.__bloomF)-self.__setBits)/len(self.__bloomF)
        # Equation A
        falsePosRate = (1-phi)**self.__numHashes

        return falsePosRate 
       
    # Returns the current number of bits ACTUALLY set in this Bloom Filter
    def numBitsSet(self):

        return self.__setBits 
    

def __main():
    numKeys = 100000
    numHashes = 4
    maxFalse = .05
    
    bloom=BloomFilter(numKeys, numHashes, maxFalse) 
    
    # read the first numKeys words from the file and insert them 
    # into the Bloom Filter. Close the input file.
    
    file=open("wordlist.txt") 
    
    for i in range(numKeys): 
        bloom.insert(file.readline())
    file.close()
  

    # Print out what the PROJECTED false positive rate should 
    # THEORETICALLY be based on the number of bits that ACTUALLY ended up being set
    # in the Bloom Filter. Use the falsePositiveRate method.
    
    f= bloom.falsePositiveRate()
    print("Theoretical False Positive Rate: " + str(f)) 
 

    # Now re-open the file, and re-read the same bunch of the first numKeys 
    # words from the file and count how many are missing from the Bloom Filter, 
    # printing out how many are missing. This should report that 0 words are 
    # missing from the Bloom Filter. Don't close the input file of words since
    # in the next step we want to read the next numKeys words from the file. 
    
    wFile= open("wordlist.txt") 
    missing=0
    for i in range(numKeys): 
        word= wFile.readline() 
        if bloom.find(word)==False: missing+=1 
    print("Number of missing keys: "+ str(missing))
        
    # Now read the next numKeys words from the file, none of which 
    # have been inserted into the Bloom Filter, and count how many of the 
    # words can be (falsely) found in the Bloom Filter.
    numFalsePos=0
    for i in range(numKeys): 
        falseW=wFile.readline() 
        if bloom.find(falseW)==True: 
            numFalsePos+=1 
    
    # Print out the percentage rate of false positives.
    # THIS NUMBER MUST BE CLOSE TO THE ESTIMATED FALSE POSITIVE RATE ABOVE    
    percentFalse= numFalsePos/numKeys 
    print("Actual false positive rate: " + str(percentFalse)) 
    
if __name__ == '__main__':
    __main()       

