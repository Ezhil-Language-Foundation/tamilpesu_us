
class உடம்படும்மெய்தொன்றல்:

    def __init__(self, சொற்கள்):
        self.handelingWords = சொற்கள்
     
    def உள்ளதா(self):
        pass

    def இணை(self):        
        for typeWord in self.handelingWords.wordsTypeMaintainer.allTypes:
            for word1, word2 in zip( typeWord.wordList[:-1] , typeWord.wordList[1:] ):
                if  word1.உயிர்யீரா and  word2.உயிர்முதலா:
                    if  word2.உயிர்முதல் in ["இ","ஈ","ஐ"]:
                        self.handelingWords.currentWord = word1.சொல் + "வ்"
                    else:
                        self.handelingWords.currentWord = word1.சொல் + "ய்"


        return self.handelingWords
  