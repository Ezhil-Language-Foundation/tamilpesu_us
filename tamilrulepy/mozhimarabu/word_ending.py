# தொல்காப்பியர்_மொழியிறுதி_விதிகள் (Tholkaappiar_word_ending_rule)
# இந்நிரலாக்கம் தமிழ் மொழித் தரவுகளைத் தொல்காப்பிய விதிகளைக் கொண்டு கணினி வழியாக மொழியிறுதி எழுத்துக்களைக் கண்டறிவதற்கான நிரல் தொகுப்பாகும்.
# இந்நிரலாக்கத்தை உருவாக்கியவர்கள் - அ.பரமேசுவரன், முனைவர் த. சத்தியராஜ் (நேயக்கோ)
import tamil

# பைத்தானில் தமிழ் மொழியை உள்ளீடு செய்வதற்கு இது பயன்படுத்தப்பெற்றுள்ளது.

# இது தரவை உள்ளீடாய்த் தருவதற்குரிய பகுதி்.


def uyir_check(word):
    """
    Checks if the last letter of a given Tamil word is a 'உயிரெழுத்து(Uyir)' (vowel) character.

    This function verifies whether the last letter of the input word is one of the
    following Tamil vowels: அ, ஆ, இ, ஈ, உ, ஊ, ,எ ,ஏ, ஐ, ஒ, ஓ, or ஔ. It checks the root form of the
    last letter to determine if it belongs to the 'Uyir' character set.

    Parameters:
    word (str): The input Tamil word to be checked.

    Returns:
    bool: True if the last letter of the word is a Tamil vowel ('உயிரெழுத்து').
    False: If the last letter is not a Tamil vowel.
    """
    uyir_list = ["அ", "ஆ", "இ", "ஈ", "உ", "ஊ","எ", "ஏ", "ஐ", "ஒ", "ஓ", "ஔ"]
    last_letter = tamil.utf8.get_letters(word)[-1]
    root_words = tamil.utf8.splitMeiUyir(last_letter)
    if type(root_words) == tuple:
        root_last = root_words[-1]
    else:
        root_last = root_words
    if root_last in uyir_list:
        return True
    else:
        return False


# இது உயிர் எழுத்தில் முடியும் உயிர்மெய் எழுத்துக்களைப் பொருத்திப் பார்ப்பதற்குரிய நிரலாகும்.


def mellinam_check(word):
    """
    Checks if the last letter of a given Tamil word is a 'மெல்லினம் (Mellinam)' (nasal consonant) character.

    This function verifies whether the last letter of the input word is one of the
    following nasal consonants: ஞ், ண், ந், ம், or ன். It checks the root form of the
    last letter to determine if it belongs to the 'மெல்லினம் (Mellinam)' character set.

    Parameters:
    word (str): The input Tamil word to be checked.

    Returns:
    bool: True if the last letter of the word is a 'மெல்லினம் (Mellinam)' character.
    False: If the last letter is not a 'மெல்லினம் (Mellinam)' character.
    """
    mellinam_list = ["ஞ்", "ண்", "ந்", "ம்", "ன்"]
    last_letter = tamil.utf8.get_letters(word)[-1]
    root_words = tamil.utf8.splitMeiUyir(last_letter)
    if type(root_words) == tuple:
        root_last = root_words[-1]
    else:
        root_last = root_words
    if root_last in mellinam_list:
        return True
    else:
        return False


# இது மெல்லின எழுத்துக்களைப் பொருத்திப் பார்ப்பதற்குரிய நிரலாகும்.


def idaiyinam_check(word):
    """
    Checks if the last letter of a given Tamil word is an 'இடையினம் (Idaiyinam)' (semi-vowel) character.

    This function verifies whether the last letter of the input word is one of the
    following semi-vowels: ய் ,ர் ,ல், வ், ழ் or ள். It checks the root form of the
    last letter to determine if it belongs to the 'இடையினம் (Idaiyinam)' character set.

    Parameters:
    word (str): The input Tamil word to be checked.

    Returns:
    bool: True if the last letter of the word is an 'இடையினம் (Idaiyinam)' character.
    False: If the last letter is not an 'இடையினம் (Idaiyinam)' character.
    """
    idaiyinam_list = ["ய்", "ர்", "ல்", "வ்", "ழ்", "ள்"]
    last_letter = tamil.utf8.get_letters(word)[-1]
    root_words = tamil.utf8.splitMeiUyir(last_letter)
    if type(root_words) == tuple:
        root_last = root_words[-1]
    else:
        root_last = root_words
    if root_last in idaiyinam_list:
        return True
    else:
        return False


# இது இடையின எழுத்துக்களைப் பொருத்திப் பார்ப்பதற்குரிய நிரலாகும்.


def oorezhuthoorumozhi_check(word):
    """
    Checks if the last letter of a given Tamil word is an 'ஓரெழுத்து ஒருமொழி (oorezhuthuoorumozhi)' (long vowel) character.

    This function verifies whether the last letter of the input word is one of the
    following long vowels: ஆ, ஈ, ஊ, ஏ, ஐ, or ஓ. It checks the root form of the
    last letter to determine if it belongs to the 'ஓரெழுத்து ஒருமொழி (oorezhuthuoorumozhi)' character set.

    Parameters:
    word (str): The input Tamil word to be checked.

    Returns:
    bool: True if the last letter of the word is an 'ஓரெழுத்து ஒருமொழி (oorezhuthuoorumozhi)' character.
    False: If the last letter is not an 'ஓரெழுத்து ஒருமொழி (oorezhuthuoorumozhi)' character.
    """
    oorezhuthoorumozhi_list = ["ஆ", "ஈ", "ஊ", "ஏ", "ஐ", "ஓ"]
    last_letter = tamil.utf8.get_letters(word)[-1]
    root_words = tamil.utf8.splitMeiUyir(last_letter)
    if type(root_words) == tuple:
        root_last = root_words[-1]
    else:
        root_last = root_words
    if root_last in oorezhuthoorumozhi_list:
        return True
    else:
        return False


# இது ஓரெழுத்தொரு மொழி எழுத்துக்களைப் பொருத்திப் பார்ப்பதற்குரிய நிரலாகும்.


def alapedai_check(word):
    """
    Checks if the last letter of a given Tamil word is an 'அளபெடை (Alapedai)' (short vowel) character.

    This function verifies whether the last letter of the input word is one of the
    following short vowels: அ, இ, உ, எ, or ஒ.

    Parameters:
    word (str): The input Tamil word to be checked.

    Returns:
    bool: True if the last letter of the word is an 'அளபெடை (Alapedai)' character.
    False: If the last letter is not an 'அளபெடை (Alapedai)' character.
    """
    alapedai_list = ["அ", "இ", "உ", "எ", "ஒ"]
    last_letter = tamil.utf8.get_letters(word)[-1]
    if last_letter in alapedai_list:

        return True
    else:
        return False


# இது அளபெடை எழுத்துக்களைப் பொருத்திப் பார்ப்பதற்குரிய நிரலாகும்.


def suttu_check(word):
    """
    Checks if a given Tamil word follows the 'சுட்டெழுத்து(Suttu)' (consonant + vowel) structure.

    This function checks if the first letter is one of the short vowels (அ, இ, உ) and 
    the second letter is one of the consonants (க்,ச்,த்,ப்,வ்). It is used to validate 
    the 'சுட்டெழுத்து(Suttu)' (consonant + vowel) structure of the word.

    Parameters:
    word (str): The input Tamil word to be checked.

    Returns:
    bool: True if the word starts with a short vowel followed by a consonant.
    False: If the word does not follow the 'சுட்டெழுத்து(Suttu)' structure.
    """
    suttu_list = ["அ", "இ", "உ"]
    suttu_mey_list = ["க்", "ச்", "த்", "ப்", "வ்"]
    first_letter = tamil.utf8.get_letters(word)[0]
    second_letter = tamil.utf8.get_letters(word)[1]

    if first_letter in suttu_list and second_letter in suttu_mey_list:
        return True
    else:
        return False


# இது சுட்டு எழுத்துக்களைப் பொருத்திப் பார்ப்பதற்குரிய நிரலாகும்.


def vinaa_check(word):
    """
    Checks if the first two letters of a given Tamil word form a specific pattern: 'Vinaa'.

    This function checks if the first letter is "எ" and the second letter is one of the 
    consonants: க்,ச்,த்,ப்,வ்,ங்,ந்.

    Parameters:
    word (str): The input Tamil word to be checked.

    Returns:
    bool: True if the word follows the 'Vinaa' pattern of 'எ' followed by a consonant.
    False: If the word does not match the 'Vinaa' pattern.
    """
    vinaa_mey_list = ["க்", "ச்", "த்", "ப்", "வ்", "ங்", "ந்"]
    if len(word) < 2:
        return False
    first_letter = tamil.utf8.get_letters(word)[0]
    second_letter = tamil.utf8.get_letters(word)[1]

    if first_letter == "எ" and second_letter in vinaa_mey_list:
        return True
    else:
        return False


# இது வினா எழுத்துக்களைப் பொருத்திப் பார்ப்பதற்குரிய நிரலாகும்.

# இது இறுதியாக அனைத்து விதிகளையும் பொருத்திப் பார்த்து பதில் அளிப்பதற்குரிய நிரலாகும்.
