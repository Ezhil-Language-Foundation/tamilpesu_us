from tamil import utf8

from  tamilrulepy.joiningConstants import JoiningConstants


NotBelongsToTamil = "it's not belongs to tamil character"

class BaseLetter:
    
    def __init__(self,letter):
        self.letter = letter

    @property
    def is_voule(self):
        if self.letter in utf8.uyir_letters:
            return True
        else:
            return False
        
    @property
    def is_constant(self):
        if self.letter in utf8.mei_letters:
            return True
        else:
            return False
        
    @property
    def is_compound(self):
        if self.letter in utf8.uyirmei_letters:
            return True
        else:
            return False
    
    @property
    def voule(self):
        if self.is_voule:
            return self.letter
        elif self.is_compound:
            con , vou = utf8.splitMeiUyir(self.letter)
            return vou
        else:
            print(NotBelongsToTamil)
            
    @property
    def constant(self):
        if self.is_constant:
            return None
        elif self.is_compound:
            con , vou = utf8.splitMeiUyir(self.letter)
            return con
        else:
            print(NotBelongsToTamil)
            
    @property
    def compound(self):
        if self.is_compound:
            return  self.is_compount
        else:
            print(NotBelongsToTamil)
            


class BaseWord:    
    def __init__(self,word):
        self.word = word
        self.letters = [ BaseLetter(l) for l in utf8.get_letters(word) ]
        self.index = 0
    

    @property
    def previousLetter(self):
        return self.letters[self.index - 1]
    
    @property
    def currentLetter(self):
        return self.letters[self.index]
    
    @property
    def nextLetter(self):
        return self.letters[self.index + 1]
    
    @property
    def nextLetter( self, num ):
        #overloading if more then one or multipe paramerter comes
        # index + num -> letter
        return self.letters[self.index + num]

    @property
    def is_nextMatch(self,word):
        for i,w in enumerate( utf8.get_letters(word) ):
            if w == self.nextLetter(i):
                pass

        return True





