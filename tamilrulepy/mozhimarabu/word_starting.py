import tamil

# பைத்தானில் தமிழ் மொழியை உள்ளீடு செய்வதற்கு இது பயன்படுத்தப்பெற்றுள்ளது.

sentence = "வலை, வானம், விலை, வீடு, வெள்ளி, வேம்பு, வையம், வௌவுதல், வேவ்வாறு ஏ ஐ ஓ யான், யாண்டு, யாறு, கொல்லாது"
# இது தரவை உள்ளீடாய்த் தருவதற்குரிய பகுதி்.


def uyirezhuthu_check(word):
    """
    Checks if the first letter of a given Tamil word is a 'உயிரெழுத்து(Uyirezhuthu)' (vowel) character.

    'உயிரெழுத்து' refers to the vowels in the Tamil script. This function checks whether 
    the first letter of the input word is one of the following Tamil vowels:
    அ, ஆ, இ, ஈ, உ, ஊ, ஏ, ஐ, ஒ, ஓ, or ஔ.

    Parameters:
    word (str): The input Tamil word to be checked.

    Returns:
    bool: True if the first letter of the word is a Tamil vowel ('உயிரெழுத்து Uyirezhuthu').
    None: If the first letter is not a Tamil vowel.
    """
    உயிர்_முதலெழுத்து = ["அ", "ஆ", "இ", "ஈ", "உ", "ஊ", "ஏ", "ஐ", "ஒ", "ஓ", "ஔ"]
    first_letter = tamil.utf8.get_letters(word)[0]
    if first_letter in உயிர்_முதலெழுத்து:
        return True
    else:
        return None


# இது உயிர் எழுத்துக்களை முதலாகக் கொண்ட நிரலாக்கம்.


def uyirmei_ka_check(word):
    """
    Checks if the first letter of a given Tamil word is a 'உயிர்மெய் (Uyirmei)' (consonant-vowel) 
    character from the 'க் (Ka)' series in the Tamil script.

    This function verifies whether the first letter of the input word is one of the
    following consonant-vowel combinations starting with 'க் (Ka)' in the Tamil script:
    க, கா, கி, கீ, கு, கூ, கெ, கே, கை, கொ, கோ, or கௌ.

    Parameters:
    word (str): The input Tamil word to be checked.

    Returns:
    bool: True if the first letter of the word is one of the specified 'க் (Ka)' series characters.
    None: If the first letter is not a 'க் (Ka)' series consonant-vowel combination.
    """
    உயிர்மெய்_முதலெழுத்து_கவரிசை = [
        "க",
        "கா",
        "கி",
        "கீ",
        "கு",
        "கூ",
        "கெ",
        "கே",
        "கை",
        "கொ",
        "கோ",
        "கௌ",
    ]
    first_letter = tamil.utf8.get_letters(word)[0]
    if first_letter in உயிர்மெய்_முதலெழுத்து_கவரிசை:
        return True
    else:
        return None


# இது கவரிசை எழுத்துக்களை முதலாகக் கொண்ட நிரலாக்கம்.


def uyirmei_sa_check(word):
    """
    Checks if the first letter of a given Tamil word is a 'உயிர்மெய் (Uyirmei)' (consonant-vowel) 
    character from the 'ச் (Sa)' series in the Tamil script.

    This function verifies whether the first letter of the input word is one of the
    following consonant-vowel combinations starting with 'ச் (Sa)' in the Tamil script:
    ச, சா, சி, சீ, சு, சூ, செ, சே, சொ, சோ.

    Parameters:
    word (str): The input Tamil word to be checked.

    Returns:
    bool: True if the first letter of the word is one of the specified 'ச் (Sa)' series characters.
    None: If the first letter is not a 'ச் (Sa)' series consonant-vowel combination.
    """
    உயிர்மெய்_முதலெழுத்து_சவரிசை = [
        "ச",
        "சா",
        "சி",
        "சீ",
        "சு",
        "சூ",
        "செ",
        "சே",
        "சொ",
        "சோ",
    ]
    first_letter = tamil.utf8.get_letters(word)[0]
    if first_letter in உயிர்மெய்_முதலெழுத்து_சவரிசை:
        return True
    else:
        return None


# இது சவரிசை எழுத்துக்களை முதலாகக் கொண்ட நிரலாக்கம்.


def uyirmei_nga_check(word):
    """
    Checks if the first letter of a given Tamil word is a 'உயிர்மெய் (Uyirmei)' (consonant-vowel) 
    character from the 'ஞ் (Nga)' series in the Tamil script.

    This function verifies whether the first letter of the input word is one of the
    following consonant-vowel combinations starting with 'ஞ் (Nga)' in the Tamil script:
    ஞா, ஞெ, ஞொ.

    Parameters:
    word (str): The input Tamil word to be checked.

    Returns:
    bool: True if the first letter of the word is one of the specified 'ஞ் (Nga)' series characters.
    None: If the first letter is not a 'ஞ் (Nga)' series consonant-vowel combination.
    """
    உயிர்மெய்_முதலெழுத்து_ஞவரிசை = ["ஞா", "ஞெ", "ஞொ"]
    first_letter = tamil.utf8.get_letters(word)[0]
    if first_letter in உயிர்மெய்_முதலெழுத்து_ஞவரிசை:
        return True
    else:
        return None


# இது ஞவரிசை எழுத்துக்களை முதலாகக் கொண்ட நிரலாக்கம்.


def uyirmei_ta_check(word):
    """
    Checks if the first letter of a given Tamil word is a 'உயிர்மெய் (Uyirmei)' (consonant-vowel) 
    character from the 'த் (Tha)' series in the Tamil script.

    This function verifies whether the first letter of the input word is one of the
    following consonant-vowel combinations starting with 'த் (Tha)' in the Tamil script:
    த, தா, தி, தீ, து, தூ, தெ, தே, தை, தொ, தோ, தௌ.

    Parameters:
    word (str): The input Tamil word to be checked.

    Returns:
    bool: True if the first letter of the word is one of the specified 'த் (Tha)' series characters.
    None: If the first letter is not a 'த் (Tha)' series consonant-vowel combination.
    """
    உயிர்மெய்_முதலெழுத்து_தவரிசை = [
        "த",
        "தா",
        "தி",
        "தீ",
        "து",
        "தூ",
        "தெ",
        "தே",
        "தை",
        "தொ",
        "தோ",
        "தௌ",
    ]
    first_letter = tamil.utf8.get_letters(word)[0]
    if first_letter in உயிர்மெய்_முதலெழுத்து_தவரிசை:
        return True
    else:
        return None


# இது தவரிசை எழுத்துக்களை முதலாகக் கொண்ட நிரலாக்கம்.


def uyirmei_na_check(word):
    """
    Checks if the first letter of a given Tamil word is a 'உயிர்மெய் (Uyirmei)' (consonant-vowel) 
    character from the 'ந் (Na)' series in the Tamil script.

    This function verifies whether the first letter of the input word is one of the
    following consonant-vowel combinations starting with 'ந் (Na)' in the Tamil script:
    ந, நா, நி, நீ, நு, நூ, நெ, நே, நை, நொ, நோ, நௌ.

    Parameters:
    word (str): The input Tamil word to be checked.

    Returns:
    bool: True if the first letter of the word is one of the specified 'ந் (Na)' series characters.
    None: If the first letter is not a 'ந் (Na)' series consonant-vowel combination.
    """
    உயிர்மெய்_முதலெழுத்து_நவரிசை = [
        "ந",
        "நா",
        "நி",
        "நீ",
        "நு",
        "நூ",
        "நெ",
        "நே",
        "நை",
        "நொ",
        "நோ",
        "நௌ",
    ]
    first_letter = tamil.utf8.get_letters(word)[0]
    if first_letter in உயிர்மெய்_முதலெழுத்து_நவரிசை:
        return True
    else:
        return None


# இது நவரிசை எழுத்துக்களை முதலாகக் கொண்ட நிரலாக்கம்.


def uyirmei_pa_check(word):
    """
    Checks if the first letter of a given Tamil word is a 'உயிர்மெய் (Uyirmei)' (consonant-vowel) 
    character from the 'ப் (Pa)' series in the Tamil script.

    This function verifies whether the first letter of the input word is one of the
    following consonant-vowel combinations starting with 'ப் (Pa)' in the Tamil script:
    ப, பா, பி, பீ, பு, பூ, பெ, பே, பை, பொ, போ, பௌ.

    Parameters:
    word (str): The input Tamil word to be checked.

    Returns:
    bool: True if the first letter of the word is one of the specified 'ப் (Pa)' series characters.
    None: If the first letter is not a 'ப் (Pa)' series consonant-vowel combination.
    """
    உயிர்மெய்_முதலெழுத்து_பவரிசை = [
        "ப",
        "பா",
        "பி",
        "பீ",
        "பு",
        "பூ",
        "பெ",
        "பே",
        "பை",
        "பொ",
        "போ",
        "பௌ",
    ]
    first_letter = tamil.utf8.get_letters(word)[0]
    if first_letter in உயிர்மெய்_முதலெழுத்து_பவரிசை:
        return True
    else:
        return None


# இது பவரிசை எழுத்துக்களை முதலாகக் கொண்ட நிரலாக்கம்.


def uyirmei_ma_check(word):
    """
    Checks if the first letter of a given Tamil word is a 'உயிர்மெய் (Uyirmei)' (consonant-vowel) 
    character from the 'ம் (Ma)' series in the Tamil script.

    This function verifies whether the first letter of the input word is one of the
    following consonant-vowel combinations starting with 'ம் (Ma)' in the Tamil script:
    ம, மா, மி, மீ, மு, மூ, மெ, மே, மை, மொ, மோ, மௌ.

    Parameters:
    word (str): The input Tamil word to be checked.

    Returns:
    bool: True if the first letter of the word is one of the specified 'ம் (Ma)' series characters.
    None: If the first letter is not a 'ம் (Ma)' series consonant-vowel combination.
    """
    உயிர்மெய்_முதலெழுத்து_மவரிசை = [
        "ம",
        "மா",
        "மி",
        "மீ",
        "மு",
        "மூ",
        "மெ",
        "மே",
        "மை",
        "மொ",
        "மோ",
        "மௌ",
    ]
    first_letter = tamil.utf8.get_letters(word)[0]
    if first_letter in உயிர்மெய்_முதலெழுத்து_மவரிசை:
        return True
    else:
        return None


# இது மவரிசை எழுத்துக்களை முதலாகக் கொண்ட நிரலாக்கம்.


def uyirmei_ya_check(word):
    """
    Checks if the first letter of a given Tamil word is a 'உயிர்மெய் (Uyirmei)' (consonant-vowel) 
    character from the 'ய் (Ya)' series in the Tamil script.

    This function verifies whether the first letter of the input word is the consonant-vowel
    combination starting with 'ய் (Ya)' in the Tamil script: யா.

    Parameters:
    word (str): The input Tamil word to be checked.

    Returns:
    bool: True if the first letter of the word is the specified 'ய் (Ya)' series character.
    None: If the first letter is not the 'ய் (Ya)' series consonant-vowel combination.
    """
    உயிர்மெய்_முதலெழுத்து_யவரிசை = ["யா"]
    first_letter = tamil.utf8.get_letters(word)[0]
    if first_letter in உயிர்மெய்_முதலெழுத்து_யவரிசை:
        return True
    else:
        return None


# இது யவரிசை எழுத்துக்களை முதலாகக் கொண்ட நிரலாக்கம்.


def uyirmei_va_check(word):
    """
    Checks if the first letter of a given Tamil word is a 'உயிர்மெய் (Uyirmei)' (consonant-vowel) 
    character from the 'வ் (Va)' series in the Tamil script.

    This function verifies whether the first letter of the input word is one of the
    following consonant-vowel combinations starting with 'வ் (Va)' in the Tamil script:
    வ, வா, வி, வீ, வெ, வே, வை, வௌ.

    Parameters:
    word (str): The input Tamil word to be checked.

    Returns:
    bool: True if the first letter of the word is one of the specified 'வ் (Va)' series characters.
    None: If the first letter is not a 'வ் (Va)' series consonant-vowel combination.
    """
    உயிர்மெய்_முதலெழுத்து_வவரிசை = ["வ", "வா", "வி", "வீ", "வெ", "வே", "வை", "வௌ"]
    first_letter = tamil.utf8.get_letters(word)[0]
    if first_letter in உயிர்மெய்_முதலெழுத்து_வவரிசை:
        return True
    else:
        return None


# இது வவரிசை எழுத்துக்களை முதலாகக் கொண்ட நிரலாக்கம்.


# இது வவரிசை எழுத்துக்களை முதலாகக் கொண்ட நிரலாக்கம்.

# இது உயிர் எழுத்தில் முடியும் உயிர்மெய் எழுத்துக்களைப் பொருத்திப் பார்ப்பதற்குரிய நிரலாகும்.
# வேவ்வாறு True > False
# இதுகுறித்த தெளிவு தேவை. இதற்குப் புதியதாக விதி எழுதுதல் வேண்டும்.
