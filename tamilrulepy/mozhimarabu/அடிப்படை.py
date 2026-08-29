from tamilrulepy.mozhimarabu.சொல்லமைப்பு import சொல்குறிப்பு
from tamilrulepy.நூன்மரபு.நூன்மரபு import உயிர்மெய்யாதல், எழுத்துகள்

 
def சொற்களையிணை(சொல்1,சொல்2):
    சொல்1 = எழுத்துகள்(சொல்1)
    சொல்2 = எழுத்துகள்(சொல்2) 
    சொல் = "".join([சொல்1[:-1], உயிர்மெய்யாதல்( சொல்1[-1],சொல்2[0]), சொல்2[1:]])
    return சொல்



class WordClasifier:
    # சொல்குறிப்பு
    def WasEndingWithVU(self):
        if self.உயிர்யீரு == "உ":
            return "EndingWithVU"

    