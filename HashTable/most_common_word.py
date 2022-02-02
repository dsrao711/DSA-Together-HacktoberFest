class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        
        # remove punctuations
        clean_sentence = ''.join([p.lower() if p.isalnum() else ' ' for p in paragraph])
        print(clean_sentence)
        
        hashmap = {}
        
        # get words and add in hashmap 
        for word in clean_sentence.split():
            if word not in banned:
                if word in hashmap : 
                    hashmap[word] += 1
                else:
                    hashmap[word]  = 1
            
        
        # get the count 
        return max(hashmap.items(), key=operator.itemgetter(1))[0]
        

        
    