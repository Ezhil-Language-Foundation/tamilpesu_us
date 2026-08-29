from tamilrulepy.mozhimarabu.சொற்கள்த்தொகுப்பு import சொற்களைத்தோற்றுவித்தல், சொற்களைப்பராமரித்தல்த்தல்
from tamilrulepy.mozhimarabu.சொல்லமைப்பு import சொல்குறிப்பு
from tamilrulepy.mozhimarabu.அடிப்படை import சொற்களையிணை
from tamilrulepy.பயன்பாடுகள் import சாரியை
from tamilrulepy.பயன்பாடுகள்.உகரம்நீங்கள் import உகரம்நீங்கள்
from tamilrulepy.பயன்பாடுகள்.உடம்படும்மெய்தொன்றல் import உடம்படும்மெய்தொன்றல்
from abc import abstractmethod


class புணர்ச்சிஅடிப்படை:
    def __init__(self ,சொற்கள்):
        self.சொற்கள் = சொற்கள்
        self.சொற்கள்_தோற்றுவித்தல் = சொற்களைத்தோற்றுவித்தல்()
        self.சொற்கள்_பராமரித்தல்த்தல் = சொற்களைப்பராமரித்தல்த்தல்()
        self.சொற்கள்_தோற்றுவித்தல்.set_state(self.சொற்கள்)
        self.handelingWords = self.சொற்கள்_தோற்றுவித்தல்.get_state()

    @abstractmethod
    def isApplicable(self):
        pass

    @abstractmethod
    def விதிகள்(self):
        pass

    def புதிப்பி(self):
        self.சொற்கள்_பராமரித்தல்த்தல்.இனை(self.handelingWords)
        self.சொற்கள்_தோற்றுவித்தல்.set_state(self.சொற்கள்)
        self.handelingWords = self.சொற்கள்_தோற்றுவித்தல்.get_state()

    

    def word(self):
       
        சொற்கள்_ = []
        for typeWord in self.handelingWords.wordsTypeMaintainer.allTypes:
            சொல்_ = None
            for wordlist in typeWord.wordList:
                
                if சொல்_ == None:
                    சொல்_ = சொல்குறிப்பு(wordlist.சொல்)
                else :
                    if ( சொல்_.மெய்யீரா and wordlist.உயிர்முதலா ):
                        
                        சொல்_.சொல் = சொற்களையிணை( சொல்_.சொல் , wordlist.சொல் )
                    else:
                        சொல்_.சொல் += wordlist.சொல்

            சொற்கள்_.append(சொல்_.சொல்)

        return சொற்கள்_
        
 
    def விளக்கம்(self):
        pass


class Caseபுணர்ச்சி(புணர்ச்சிஅடிப்படை):
    pass

class LetterPartical(புணர்ச்சிஅடிப்படை):
    pass


class சாரிப்புணர்ச்சி(புணர்ச்சிஅடிப்படை):

    def isApplicable(self):
        if self.handelingWords.grammerIndentification( சாரியை.allParticals ):
            return True  
        else:
            return False

    def applyRule(self):
        self.handelingWords = சாரியை.Particlas(
            self.handelingWords.nextWord)(
            self.handelingWords
            ).இணை()
         
        self.handelingWords = உகரம்நீங்கள்(self.handelingWords).இணை()
        self.handelingWords = உடம்படும்மெய்தொன்றல்(self.handelingWords).இணை()
        

def புணர்ச்சி(சொற்கள்):
           
        if len(சொற்கள்) == 1:
            pass
        
        if len(சொற்கள்) == 2:
            pass
        
        if len(சொற்கள்) == 3:
            for புணர்ச்சிவிதி in [ சாரிப்புணர்ச்சி ]:
                புணர்ச்சி = புணர்ச்சிவிதி(சொற்கள்)
                if புணர்ச்சி.isApplicable:
                    புணர்ச்சி.applyRule()
                    print( புணர்ச்சி.word() )
                    # TODO remove the print
                    #return புணர்ச்சி.சொல்()

        
        if len(சொற்கள்) == 4:
            pass
        





