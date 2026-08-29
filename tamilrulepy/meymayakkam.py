import tamil

# 1) க் + க
# ஒரு சொல்லில் க் எழுத்துக்குப் பின்பு க எழுத்து மயங்கி வரும். எ-டு. அக்கா, ஆக்கம்

#word=input("Enter the word to check: ")

def meymayakkam_checker(word_letters, letter, allowed_list, Mei=["க்", "ங்", "ச்", "ஞ்", "ட்", "ண்", "த்", "ந்", "ப்", "ம்", "ய்", "ர்", "ல்", "வ்", "ழ்", "ள்", "ற்","ன்"] ): 
    """
    meymayakkam_checker is generic utility function used to do the regular check.
    All the meymayakkam rule follows a similar pattern like once a mei words came it needs to be followed with some words

    This function helps to do the check that and since it is writen in generic way, all the rules will be using this for checking.

        Parameters:
            word_letters list(str) : word as a list with individual letters as elements 
            letter (str) : Rule specific mei letter we want to check
            allowed_list list(str) : list of letters which are allowed to follow the mei letter as per tholkappiyar rule

        Returns :
            result (bool):
                True - If the mei letter is followed by correct allowed letters only
                False - If the mei letter is not followed by the allowed letters 
    """
    ind=word_letters.index(letter)
    if word_letters[ind+1] in Mei:# Need to check on this point since some are overlapping. we can use sets here
	    return False
    else:
	    root_words=tamil.utf8.splitMeiUyir(word_letters[ind+1])
	    if type(root_words)==tuple:
		    root_last=root_words[0]
	    else:
		    root_last=root_words
	    if root_last in allowed_list: 
		    return True
	    else:
		    return False

#"மெய்ம்மயக்கம்1": "க்+க"
def meymayakkam1(word):
    """
    meymayakkam1 is the implementation of Tholkappiyar rule of mei mayakkam for the letter "க்"

    The Letter  "க்" must be followed by any derivatives of "க" i.e க,கா,கி,...  

        Parameters:
            word (str) : word you want to check the grammar correctness

        Returns :
            result (bool):
                True - The rule matches and it it grammatically correct for "க்"
                False - The rule matches and it is not correct for the letter "க்"
                None - The rule doesn't apply since there is no "க்" in the word
    """
    letters=tamil.utf8.get_letters(word)
    if "க்" in letters and letters.index("க்")!=len(letters)-1:
        return meymayakkam_checker(letters, "க்", ["க்"])
    else:
		    return None
		    
#"மெய்ம்மயக்கம்2": "ங்+கங"
def meymayakkam2(word):
    """
    meymayakkam2 is the implementation of Tholkappiyar rule of mei mayakkam for the letter "ங்"

    The Letter  "ங்" must be followed by any derivatives of "க", "ங" i.e க,கா,கி,...  (or)ங, ஙா ஙி ,...

        Parameters:
            word (str) : word you want to check the grammar correctness

        Returns :
            result (bool):
                True - The rule matches and it it grammatically correct for "ங்"
                False - The rule matches and it is not correct for the letter "ங்"
                None - The rule doesn't apply since there is no "ங்" in the word
    """
    letters=tamil.utf8.get_letters(word)
    if "ங்" in letters and letters.index("ங்")!=len(letters)-1:
        return meymayakkam_checker(letters, "ங்", ["க்", "ங்"])
    else:
		    return None

#"மெய்ம்மயக்கம்3": "ச்+ச"
def meymayakkam3(word):
    """
    meymayakkam3 is the implementation of Tholkappiyar rule of mei mayakkam for the letter "ச்" 

    The Letter  "ச்" must be followed by any derivatives of "ச" i.e ச, சா, சி, சீ,...  

        Parameters:
            word (str) : word you want to check the grammar correctness

        Returns :
            result (bool):
                True - The rule matches and it it grammatically correct for "ச்" 
                False - The rule matches and it is not correct for the letter "ச்"
                None - The rule doesn't apply since there is no "ச்" in the word
    """
    letters=tamil.utf8.get_letters(word)
    if "ச்" in letters and letters.index("ச்")!=len(letters)-1:
        return meymayakkam_checker(letters, "ச்", ["ச்"])
    else:
		    return None

#"மெய்ம்மயக்கம்4": "ஞ்+சஞய
def meymayakkam4(word):
    """
    meymayakkam4 is the implementation of Tholkappiyar rule of mei mayakkam for the letter "ஞ்"  

    The Letter  "ஞ்" must be followed by any derivatives of "ச","ஞ","ய" (i.e) ச, சா, சி,... (or) ஞ 	ஞா 	ஞி,... (or) ய 	யா 	யி,...

        Parameters:
            word (str) : word you want to check the grammar correctness

        Returns :
            result (bool):
                True - The rule matches and it it grammatically correct for "ஞ்" 
                False - The rule matches and it is not correct for the letter "ஞ்" 
                None - The rule doesn't apply since there is no "ஞ்"  in the word
    """
    letters=tamil.utf8.get_letters(word)
    if "ஞ்" in letters and letters.index("ஞ்")!=len(letters)-1:
        return meymayakkam_checker(letters, "ஞ்", ["ச்","ஞ்","ய்"])
    else:
		    return None
#"மெய்ம்மயக்கம்5": "ட்+கசடப"
def meymayakkam5(word):
    """
    meymayakkam5 is the implementation of Tholkappiyar rule of mei mayakkam for the letter "ட்"

    The Letter  "ட்" must be followed by any derivatives of "க", "ச", "ட", "ப" (i.e) க 	கா 	கி,... (or) ... (or) ய 	யா 	யி,...

        Parameters:
            word (str) : word you want to check the grammar correctness

        Returns :
            result (bool):
                True - The rule matches and it it grammatically correct for "ட்" 
                False - The rule matches and it is not correct for the letter "ட்" 
                None - The rule doesn't apply since there is no "ட்"  in the word
    """
    letters=tamil.utf8.get_letters(word)
    if "ட்" in letters and letters.index("ட்")!=len(letters)-1:
        return meymayakkam_checker(letters, "ட்", ["க்", "ச்", "ட்", "ப்"])
    else:
		    return None

#"மெய்ம்மயக்கம்6": "ண்+கசஞடணபமயவ"
def meymayakkam6(word):
    """
    meymayakkam6 is the implementation of Tholkappiyar rule of mei mayakkam for the letter "ண்"

    The Letter  "ண்" must be followed by any derivatives of "க்","ச்","ஞ்","ட்","ண்","ப்","ம்","ய்","வ்" (i.e) க, கா,	கி... (or) ச,சா ,சி... (or) ஞ ,ஞா,ஞி... (or) ட ,டா,	டி... (or) ண ,ணா ,ணி... (or) ப,	பா,	பி... (or) ம,	மா,	மி ... (or) ய,	யா,	யி... (or) வ,	வா,	வி...

        Parameters:
            word (str) : word you want to check the grammar correctness

        Returns :
            result (bool):
                True - The rule matches and it it grammatically correct for "ண்"
                False - The rule matches and it is not correct for the letter "ண்"
                None - The rule doesn't apply since there is no "ண்" in the word
 
    """
    letters=tamil.utf8.get_letters(word)
    if "ண்" in letters and letters.index("ண்")!=len(letters)-1:
        return meymayakkam_checker(letters, "ண்", ["க்", "ச்", "ஞ்", "ட்", "ண்", "ப்", "ம்", "ய்", "வ்"])
    else:
		    return None

#"மெய்ம்மயக்கம்7": "த்+த"
def meymayakkam7(word):
    """
    meymayakkam7 is the implementation of Tholkappiyar rule of mei mayakkam for the letter "த்"

    The Letter  "த்" must be followed by any derivatives of "த்" (i.e) த,	த,,	தி...

        Parameters:
            word (str) : word you want to check the grammar correctness

        Returns :
            result (bool):
                True - The rule matches and it it grammatically correct for "த்"
                False - The rule matches and it is not correct for the letter "த்"
                None - The rule doesn't apply since there is no "த்" in the word
    """
    letters=tamil.utf8.get_letters(word)
    if "த்" in letters and letters.index("த்")!=len(letters)-1:
        return meymayakkam_checker(letters, "த்", ["த்"])
    else:
		    return None

#"மெய்ம்மயக்கம்8": "ந்+தநய"
def meymayakkam8(word):
    """
    meymayakkam8 is the implementation of Tholkappiyar rule of mei mayakkam for the letter "ந்"

    The Letter  "ந்" must be followed by any derivatives of "த்","ந்","ய்" (i.e) த,	த,,	தி... (or) ந,	நா,	நி... (or) ய,	யா,	யி...

        Parameters:
            word (str) : word you want to check the grammar correctness

        Returns :
            result (bool):
                True - The rule matches and it it grammatically correct for "ந்"
                False - The rule matches and it is not correct for the letter "ந்"
                None - The rule doesn't apply since there is no "ந்" in the word
    """
    letters=tamil.utf8.get_letters(word)
    if "ந்" in letters and letters.index("ந்")!=len(letters)-1:
        return meymayakkam_checker(letters, "ந்", ["த்", "ந்", "ய்"])
    else:
		    return None

#"மெய்ம்மயக்கம்9": "ப்+ப"
def meymayakkam9(word):
    """
    meymayakkam9 is the implementation of Tholkappiyar rule of mei mayakkam for the letter "ப்"

    The Letter  "ப்" must be followed by any derivatives of "ப்" (i.e) ப,	பா,	பி...

        Parameters:
            word (str) : word you want to check the grammar correctness

        Returns :
            result (bool):
                True - The rule matches and it it grammatically correct for "ப்"
                False - The rule matches and it is not correct for the letter "ப்"
                None - The rule doesn't apply since there is no "ப்" in the word
    """
    letters=tamil.utf8.get_letters(word)
    if "ப்" in letters and letters.index("ப்")!=len(letters)-1:
        return meymayakkam_checker(letters, "ப்", ["ப்"])
    else:
		    return None

#"மெய்ம்மயக்கம்10": "ம்+பமயவ"
def meymayakkam10(word):
    """
    meymayakkam10 is the implementation of Tholkappiyar rule of mei mayakkam for the letter "ம்"

    The Letter  "ம்" must be followed by any derivatives of "ப்","ம்","ய்","வ்" (i.e) ப,	பா,	பி... (or) ம,	மா,	மி ... (or) ய,	யா,	யி... (or) வ,	வா,	வி...

        Parameters:
            word (str) : word you want to check the grammar correctness

        Returns :
            result (bool):
                True - The rule matches and it it grammatically correct for "ம்"
                False - The rule matches and it is not correct for the letter "ம்"
                None - The rule doesn't apply since there is no "ம்" in the word
    """
    letters=tamil.utf8.get_letters(word)
    if "ம்" in letters and letters.index("ம்")!=len(letters)-1:
        return meymayakkam_checker(letters, "ம்", ["ப்", "ம்", "ய்", "வ்"])
    else:
		    return None

#"மெய்ம்மயக்கம்11": "ய்+கசதபஞநமயவங"
def meymayakkam11(word):
    """
    meymayakkam11 is the implementation of Tholkappiyar rule of mei mayakkam for the letter "ய்"

    The Letter  "ய்" must be followed by any derivatives of "க்","ங்","ச்","ஞ்","த்","ந்","ப்","ம்","ய்","வ்" (i.e) க, கா,	கி... (or) ங,ஙா,ஙி,... (or) ச,சா ,சி... (or) ஞ ,ஞா,ஞி... (or) த,	த,,	தி... (or) ந,	நா,	நி... (or) ப,	பா,	பி... (or) ம,	மா,	மி ... (or) ய,	யா,	யி... (or) வ,	வா,	வி...

        Parameters:
            word (str) : word you want to check the grammar correctness

        Returns :
            result (bool):
                True - The rule matches and it it grammatically correct for "ய்"
                False - The rule matches and it is not correct for the letter "ய்"
                None - The rule doesn't apply since there is no "ய்" in the word
    """
    letters=tamil.utf8.get_letters(word)
    if "ய்" in letters and letters.index("ய்")!=len(letters)-1:
        return meymayakkam_checker(letters, "ய்", ["க்", "ங்", "ச்", "ஞ்", "த்", "ந்", "ப்", "ம்", "ய்", "வ்"])
    else:
		    return None

#"மெய்ம்மயக்கம்12": "ர்+கசதபஞநமயவங"
def meymayakkam12(word):
    """
    meymayakkam12 is the implementation of Tholkappiyar rule of mei mayakkam for the letter "ர்"

    The Letter  "ர்" must be followed by any derivatives of "க்","ங்","ச்","ஞ்","த்","ந்","ப்","ம்","ய்","வ்" (i.e) க, கா,	கி... (or) ங,ஙா,ஙி,... (or) ச,சா ,சி... (or) ஞ ,ஞா,ஞி... (or) த,	த,,	தி... (or) ந,	நா,	நி... (or) ப,	பா,	பி... (or) ம,	மா,	மி ... (or) ய,	யா,	யி... (or) வ,	வா,	வி...

        Parameters:
            word (str) : word you want to check the grammar correctness

        Returns :
            result (bool):
                True - The rule matches and it it grammatically correct for "ர்"
                False - The rule matches and it is not correct for the letter "ர்"
                None - The rule doesn't apply since there is no "ர்" in the word
    """
    letters=tamil.utf8.get_letters(word)
    if "ர்" in letters and letters.index("ர்")!=len(letters)-1:
        return meymayakkam_checker(letters, "ர்", ["க்", "ங்", "ச்", "ஞ்", "த்", "ந்", "ப்", "ம்", "ய்", "வ்"])
    else:
		    return None

#"மெய்ம்மயக்கம்13": "ழ்+கசதபஞநமயவங"
def meymayakkam13(word):
    """
    meymayakkam13 is the implementation of Tholkappiyar rule of mei mayakkam for the letter "ழ்"

    The Letter  "ழ்" must be followed by any derivatives of "க்","ங்","ச்","ஞ்","த்","ந்","ப்","ம்","ய்","வ்" (i.e) க, கா,	கி... (or) ங,ஙா,ஙி,... (or) ச,சா ,சி... (or) ஞ ,ஞா,ஞி... (or) த,	த,,	தி... (or) ந,	நா,	நி... (or) ப,	பா,	பி... (or) ம,	மா,	மி ... (or) ய,	யா,	யி... (or) வ,	வா,	வி...

        Parameters:
            word (str) : word you want to check the grammar correctness

        Returns :
            result (bool):
                True - The rule matches and it it grammatically correct for "ழ்"
                False - The rule matches and it is not correct for the letter "ழ்"
                None - The rule doesn't apply since there is no "ழ்" in the word
    """
    letters=tamil.utf8.get_letters(word)
    if "ழ்" in letters and letters.index("ழ்")!=len(letters)-1:
        return meymayakkam_checker(letters, "ழ்", ["க்", "ங்", "ச்", "ஞ்", "த்", "ந்", "ப்", "ம்", "ய்", "வ்"])
    else:
		    return None

#"மெய்ம்மயக்கம்14": "வ்+வ"
def meymayakkam14(word):
    """
    meymayakkam14 is the implementation of Tholkappiyar rule of mei mayakkam for the letter "வ்"

    The Letter  "வ்" must be followed by any derivatives of "வ்" (i.e) வ,	வா,	வி...

        Parameters:
            word (str) : word you want to check the grammar correctness

        Returns :
            result (bool):
                True - The rule matches and it it grammatically correct for "வ்"
                False - The rule matches and it is not correct for the letter "வ்"
                None - The rule doesn't apply since there is no "வ்" in the word
    """
    letters=tamil.utf8.get_letters(word)
    if "வ்" in letters and letters.index("வ்")!=len(letters)-1:
        return meymayakkam_checker(letters, "வ்", ["வ்"])
    else:
		    return None

#"மெய்ம்மயக்கம்15": "ல்+கசபலயவ"
def meymayakkam15(word):
    """
    meymayakkam15 is the implementation of Tholkappiyar rule of mei mayakkam for the letter "ல்"

    The Letter  "ல்" must be followed by any derivatives of "க்","ச்","ப்","ல்","ய்","வ்" (i.e) க, கா,	கி... (or) ச,சா ,சி... (or) ப,	பா,	பி... (or) ல,	லா,	லி... (or) ய,	யா,	யி... (or) வ,	வா,	வி...

        Parameters:
            word (str) : word you want to check the grammar correctness

        Returns :
            result (bool):
                True - The rule matches and it it grammatically correct for "ல்"
                False - The rule matches and it is not correct for the letter "ல்"
                None - The rule doesn't apply since there is no "ல்" in the word
 
    """
    letters=tamil.utf8.get_letters(word)
    if "ல்" in letters and letters.index("ல்")!=len(letters)-1:
        return meymayakkam_checker(letters, "ல்", ["க்", "ச்", "ப்", "ல்", "ய்", "வ்"])
    else:
		    return None

#"மெய்ம்மயக்கம்16": "ள்+கசபளயவ"
def meymayakkam16(word):
    """
    meymayakkam16 is the implementation of Tholkappiyar rule of mei mayakkam for the letter "ள்"

    The Letter  "ள்" must be followed by any derivatives of "க்","ச்","ப்","ள்","ய்","வ்" (i.e) க, கா,	கி... (or) ச,சா ,சி... (or) ப,	பா,	பி... (or) ள,	ளா,	ளி... (or) ய,	யா,	யி... (or) வ,	வா,	வி...

        Parameters:
            word (str) : word you want to check the grammar correctness

        Returns :
            result (bool):
                True - The rule matches and it it grammatically correct for "ள்"
                False - The rule matches and it is not correct for the letter "ள்"
                None - The rule doesn't apply since there is no "ள்" in the word
 
    """
    letters=tamil.utf8.get_letters(word)
    if "ள்" in letters and letters.index("ள்")!=len(letters)-1:
        return meymayakkam_checker(letters, "ள்", ["க்", "ச்", "ப்", "ள்", "ய்", "வ்"])
    else:
		    return None

#"மெய்ம்மயக்கம்17": "ற்+கசபற"
def meymayakkam17(word):
    """
    meymayakkam17 is the implementation of Tholkappiyar rule of mei mayakkam for the letter "ற்"

    The Letter  "ற்" must be followed by any derivatives of "க்","ச்","ப்","ற்" (i.e) க, கா,	கி... (or) ச,சா ,சி... (or) ப,	பா,	பி... (or) ற,	றா,	றி...

        Parameters:
            word (str) : word you want to check the grammar correctness

        Returns :
            result (bool):
                True - The rule matches and it it grammatically correct for "ற்"
                False - The rule matches and it is not correct for the letter "ற்"
                None - The rule doesn't apply since there is no "ற்" in the word
    """
    letters=tamil.utf8.get_letters(word)
    if "ற்" in letters and letters.index("ற்")!=len(letters)-1:
        return meymayakkam_checker(letters, "ற்", ["க்", "ச்", "ப்", "ற்"])
    else:
		    return None

#"மெய்ம்மயக்கம்18": "ன்+கசஞபமயவறன"
def meymayakkam18(word):
    """
    meymayakkam18 is the implementation of Tholkappiyar rule of mei mayakkam for the letter "ன்"

    The Letter  "ன்" must be followed by any derivatives of "க்","ச்","ஞ்","ப்","ம்","ய்","வ்","ற்","ன்" (i.e) க, கா,	கி... (or) ச,சா ,சி... (or) ஞ ,ஞா,ஞி... (or) ப,	பா,	பி... (or) ம,	மா,	மி ... (or) ய,	யா,	யி... (or) வ,	வா,	வி... (or) ற,	றா,	றி... (or) ன,	னா,	னி...

        Parameters:
            word (str) : word you want to check the grammar correctness

        Returns :
            result (bool):
                True - The rule matches and it it grammatically correct for "ன்"
                False - The rule matches and it is not correct for the letter "ன்"
                None - The rule doesn't apply since there is no "ன்" in the word
    """
    letters=tamil.utf8.get_letters(word)
    if "ன்" in letters and letters.index("ன்")!=len(letters)-1:
        return meymayakkam_checker(letters, "ன்", ["க்", "ச்", "ஞ்", "ப்", "ம்", "ய்", "வ்", "ற்", "ன்"])
    else:
		    return None
		    
