from tamilrulepy.mozhimarabu.சொல்லமைப்பு import சொல்குறிப்பு

 

class WordsTypeDefinition:
    def __init__(self,words):
        self.wordList =  [ சொல்குறிப்பு(word) for word in words ]
        self.index = 0
        self.Type = {
        }

    @property
    def postion(self):
        return self.index
    
    @postion.setter
    def postion(self,idx):
        self.index = idx

    @property
    def explenation(self):
        if self.Type['definition'] != None:
            return self.Type['definition']
        else:
            None

    @explenation.setter
    def explenation(self,definition):
        self.Type["definition"] = definition

    @property
    def rule(self):       
        if self.Type['rule'] != None:
            return self.Type["rule"]
        else:
            None

    @rule.setter
    def rule(self, ruleNo):
        self.Type["rule"] =  ruleNo
  
    @property
    def indexWord(self):
        return self.Type['words'][self.index].மொழி
        
    @indexWord.setter
    def indexWord(self,  word): 
        self.Type['words'][self.index].மொழி = word

    @property
    def grammerIndentification(self,IndentificationList):
        for Indentification in IndentificationList:
            if Indentification in self.Type['words'][self.index].குறிப்பு:
                return True
            else:
                return False


class WordsTypeOriginator:

    def set_state(self, state):
        self.state = state

    def get_state(self):
        return WordsTypeDefinition(self.state)


class  WordsTypeMaintainer: #பராமரிப்பாளர்
    def __init__(self):
        self.typesList = []
        self.typeIndex = 0

    def addType(self, state):
        self.typesList.append( state )

    @property
    def getType(self, index):
        return self.typesList[index]

    @property
    def totalTypes(self):
        return len( self.typesList )
    
    @property
    def allTypes(self):
        return self.typesList


class சொற்கள்_நினைவகம்: # நினைவுச்சின்னம் 
    def __init__(self, சொற்கள்):
        self.actualWords = சொற்கள்
        self.wordPosition = 0

        self.wordsTypeOriginator = WordsTypeOriginator()
        self.wordsTypeMaintainer = WordsTypeMaintainer()
        
        self.wordsTypeOriginator.set_state( self.actualWords )
        self.handelingType = self.wordsTypeOriginator.get_state()
        
    @property
    def changeType(self, index):
        self.handelingType = self.wordsTypeMaintainer.getType(index)

    def saveType(self):
        self.wordsTypeMaintainer.addType( self.handelingType )
 
    def addNewType(self):
        self.wordsTypeMaintainer.addType( self.handelingType )
        self.wordsTypeOriginator.set_state( self.actualWords )
        self.handelingType = self.wordsTypeOriginator.get_state()
        
    @property
    def explination(self):
        return self.handelingType.explenation 

    @explination.setter
    def explination(self, explenation):
        self.handelingType.explenation = explenation  
    
    @property
    def rule(self):
        return self.handelingType.rule

    @rule.setter
    def rule(self, ruleNo):
        self.handelingType.rule = ruleNo

    @property
    def types(self):
        return self.wordsTypeMaintainer.totalTypes

    @property
    def handelingTypeIndex(self):
        return self.handelingType.index

    @handelingTypeIndex.setter
    def handelingTypeIndex(self,idx):
        self.handelingType.index = idx

    @property
    def handelingTypewords(self):
        return self.handelingType.wordList

    @property
    def previousWord(self):
        return self.handelingTypewords[self.wordPosition - 1 ].மொழி

    @property
    def currentWord(self):
        return self.handelingTypewords[self.wordPosition].மொழி
    
    @property
    def nextWord(self):
        return self.handelingTypewords[self.wordPosition + 1 ].மொழி

    @previousWord.setter
    def previousWord(self, word):
        self.handelingTypewords[self.wordPosition - 1].மொழி  = word

    @currentWord.setter
    def currentWord(self, word):
        self.handelingTypewords[self.wordPosition].மொழி = word
    
    @nextWord.setter
    def nextWord(self, word):
        self.handelingTypewords[ self.wordPosition + 1 ].மொழி = word


class சொற்களைத்தோற்றுவித்தல்: 

    def set_state(self,சொற்கள்):
        self.சொற்கள் =  சொற்கள்
    
    def get_state(self):
        return சொற்கள்_நினைவகம்( self.சொற்கள் )

    def restore_memento(self,memento):
        self.state = memento.state


class சொற்களைப்பராமரித்தல்த்தல்: #பராமரிப்பாளர்

    def __init__(self):
        self.சொற்கள்_நினைவகள் = []

    def இனை(self, memento):
        self.சொற்கள்_நினைவகள்.append(memento)

    def get_memento(self, index):
        return self.menetos[index]


 