
collections = ""

class WordExiestanceChecker:
    def __init__(self, word):
        self.word = word 

    def wordExist(self):

        if self.word in collections:
            pass

        elif self.word+"ம்" in collections:
            pass

        elif self.word+"மை" in collections:
            pass

        elif self.word+"உ" in collections:
            pass

        elif self.word+"ம்" in collections:
            pass


    def ParticalExist(self):
        pass

    def CaseExist(self):
        pass


class WordSegmenting(WordExiestanceChecker):
    
    def __init__(self,word):
        self.word = word
        self.index = 0
    

    def match(self,previousWordLastLetter,nestWordLastLetter):
        for letter in self.letters:
            
            if letter == previousWordLastLetter:

                if self.nextIndexLetter == "JoiningConstants":
                    pass
                if self.nextIndexLetter == nestWordLastLetter:
                    pass
                else:
                    pass

            self.index += 1
    

