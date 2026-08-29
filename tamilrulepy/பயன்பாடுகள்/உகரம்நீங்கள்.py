from tamilrulepy.நூன்மரபு.நூன்மரபு import உயிர்நீங்கள்

class  உகரம்நீங்கள்:

    def __init__(self, சொற்கள்):
        self.handelingWords = சொற்கள்
     
    def உள்ளதா(self):
        pass

    def இணை(self):        
        for typeWord in self.handelingWords.wordsTypeMaintainer.allTypes:
            for word1, word2 in zip( typeWord.wordList[:-1] , typeWord.wordList[1:] ):
                if  word1.உயிர்மெய்யீரா and word2.உயிர்முதலா:
                    UVoule = உயிர்நீங்கள்(word1.மொழியிருதி)
                    if UVoule == 'உ':
                        self.handelingWords.currentWord = word1
                
 
        return self.handelingWords
