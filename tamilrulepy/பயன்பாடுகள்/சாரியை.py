
#,"வற்று","அத்து","அம்","ஒன்","ஆன்","அக்கு","இக்கு",
# "தம்","நம்","நும்","உம்","கெழு","ஏ", "ஐ","ஞான்று"

உருபுகள் = ["இன்","வற்று","அத்து","அம்","ஆன்","அக்கு","இக்கு"]

allParticals = ["இன்","வற்று","அத்து","அம்","ஆன்","அக்கு","இக்கு"]



def Particlas(உருபு):
    return globals()[உருபு]


def சாரியை_உருபுகள்(உருபு):
    return globals()[உருபு]


class BaseParticals:

    def __init__(self, சொற்கள்):
        self.handelingWords = சொற்கள்
        self.typeNo = -1

    def changeType(self):
        if self.typeNo >= 0:
            self.handelingWords.addNewType()
        elif self.typeNo < 0:
            self.typeNo = 1
        else:
            print("*****--<>")
            # TODO remove the print

    pass



class இன்(BaseParticals):

    def உள்ளதா(self):
        pass
 
    def இணை(self):        
        for word in self.handelingWords.handelingTypewords[:-1]:
            if word.உயிர்யீரு == "ஆ":
                if self.handelingWords.nextWord == 'இன்':
                    self.changeType()
                if self.handelingWords.nextWord == 'இன்':
                    self.handelingWords.nextWord = "ன்"
                    self.changeType()


        self.handelingWords.saveType()
        return self.handelingWords
 

class வற்று(BaseParticals):

    def உருப்பு(self):
        return self.சொல்

    def உள்ளதா(self):
        pass

    def இணை( self):
        pass

    
class ஆன்(BaseParticals):
    def உருப்பு(self):
        return self.சொல்

    def உள்ளதா(self):
        pass

    def இணை( self):
        pass



class அத்து(BaseParticals):

    def உருப்பு(self):
        return self.சொல்

    def உள்ளதா(self):
        pass

    def இணை( self):
        pass






class இக்கு(BaseParticals):

    def உருப்பு(self):
        return self.சொல்

    def உள்ளதா(self):
        pass

    def இணை( self):
        pass

    
class அக்கு(BaseParticals):

    def உருப்பு(self):
        return self.சொல்

    def உள்ளதா(self):
        pass

    def இணை( self):
        pass


class அம்(BaseParticals):

    def உருப்பு(self):
        return self.சொல்

    def உள்ளதா(self):
        pass

    def இணை( self):
        pass

