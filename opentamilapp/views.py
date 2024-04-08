# -*- coding: utf-8 -*-
import os

from django.shortcuts import render
from django.http import HttpResponse, Http404

from datetime import datetime
import tamil
import codecs
import sys
import copy
import math
import re
import html
import json
import random
from tamil.utf8 import get_letters
from tamil.date import datetime as ta_datetime
from tamil import wordutils
from spell import Speller, LoadDictionary, ASpell
from solthiruthi.datastore import TamilTrie, DTrie, Queue
from solthiruthi.Ezhimai import *
from solthiruthi.resources import DICTIONARY_DATA_FILES
from solthiruthi.data_parser import *
from solthiruthi.dictionary import *
from solthiruthi.datastore import DTrie
from transliterate import azhagi, jaffna, combinational, algorithm
from ngram.Corpus import Corpus
from ngram import LetterModels
from ngram.LetterModels import *
from ngram.WordModels import *
import tamil.utf8 as utf8
from tamilsandhi.sandhi_checker import check_sandhi
from .tamilwordgrid import generate_tamil_word_grid
from .webuni import unicode_converter
from tamil.wordutils import minnal as tamil_minnal
from tamilstemmer import TamilStemmer
from opentamilweb import settings
from tamil.olini import கணக்கிடு as kanakkidu
import tamilmorse

try:
    from tamiltts import ConcatennativeTTS
    from .classifier import process_word
except Exception as ioe:
    print("process word function not imported because,", ioe)
    process_word = lambda x: x

from tamilinayavaani import SpellChecker, SpellCheckerResult
from django.views.decorators.csrf import csrf_exempt

from dateutil import parser as dateutil_parser
from anicham import yappu_venba,EerasaiType,MoovasaiType,Venba,EetruSeerAsai,Seer
from opentamilapp.kuralviews import get_adhikaram, kurals, get_pals, get_matching_kural, சீர்_பிரித்த_குறள்

def aspell_spell_check(request):
    return render(request,"opentamilapp/aspell_spell_check.html")

@csrf_exempt
def aspell_spellchecker(request):
    if request.method == 'POST':
        lang = request.POST['lang']
        text = request.POST['text']
        if lang != "ta_IN":
            json_string = json.dumps({'error':'Language '+lang+' is not supported; only takes Tamil (code ta_IN))'})
            response = HttpResponse(json_string, content_type="application/json; charset=utf-8")
            return response

        lang = "TA"
        result_dict = {'words':{}}

        result = ASpell().spellcheck(str(text))
        for word,suggl in result.items():
            result_dict['words'][word] = suggl
        json_string = json.dumps(result_dict)
        response = HttpResponse(json_string, content_type="application/json; charset=utf-8")
        return response

    assert request.method == "GET"
    text = request.GET['text']
    suggs = ASpell().spellcheck(str(text))
    return HttpResponse("RPC interface for TinyMCE Spell Checker!"+text+':'+str(suggs),content_type="plain/text; charset=utf-8")
    #return Http404("unknown request; resource not found. Use POST request!")

def tamilinayavaani_spell_check(request):
    return render(request,"opentamilapp/tamilinayavaani_spell_check.html")

@csrf_exempt
def tamilinayavaani_spellchecker(request):
    if request.method == 'POST':
        lang = request.POST['lang']
        text = request.POST['text']
        if lang != "ta_IN":
            json_string = json.dumps({'error':'Language '+lang+' is not supported; only takes Tamil (code ta_IN))'})
            response = HttpResponse(json_string, content_type="application/json; charset=utf-8")
            return response

        lang = "TA"
        result_dict = {'words':{}}

        wordlist = list(filter(len,re.split('\s+',text)))
        Lmax = len(wordlist)-1
        for itr,word in enumerate( wordlist ):
            if word.find("<") >= 0: #HTML Tags, skip
                continue
            #print("checking word %d"%itr,file=sys.stderr)
            try:
                next_word = wordlist[itr+1] if itr != Lmax else None
                ok,suggs = SpellChecker.REST_interface(word,next_word)
                suggs = suggs[0].split(',')
            except Exception as ioe:
                ok = True

            if not ok:
                word = SpellChecker.scrub_ws(word)
                suggl = list(suggs)
                result_dict['words'][word] = suggl
        json_string = json.dumps(result_dict)
        response = HttpResponse(json_string, content_type="application/json; charset=utf-8")
        return response

    assert request.method == "GET"
    text = request.GET['text']
    ok,suggs = SpellChecker.REST_interface(str(text))
    return HttpResponse("RPC interface for TinyMCE Spell Checker!"+text+':'+str(suggs)+':'+str(ok),content_type="plain/text; charset=utf-8")

def index(request):
    return render(request,"opentamilapp/first.html")

def version(request):
    return render(request,"opentamilapp/version.html",{"VERSION":tamil.VERSION})

def tamil_letters_table(request,kind='uyirmei'):
    if kind == 'uyir':
        context = {'uyir': 12, 'mei': 0}
        return render(request, "opentamilapp/letters_table.html",context)
    elif kind == 'mei':
        context = {'uyir': 1, 'mei': 18}
        return render(request, "opentamilapp/letters_table.html",context)
    assert kind == 'uyirmei'
    context = {'uyir': 12, 'mei': 18}
    return render(request,"opentamilapp/letters_table.html",context)

def vaypaadu(request):
    return render(request,"opentamilapp/vaypaadu.html")

def trans(request):
    return render(request,"opentamilapp/translite.html")


def uni(request):
    return render(request,"opentamilapp/unicode.html")


def keechu(request):
    return render(request,"opentamilapp/keechu.html")


def spl(request):
    return render(request,"opentamilapp/spell.html")


def rev(request):
    return render(request,"opentamilapp/reverse.html")


def morse_code(request):
    return render(request,"opentamilapp/morse.html")


def num(request):
    return render(request,"opentamilapp/number.html")


def anag(request):
    return render(request,"opentamilapp/anagram.html")


def unig(request):
    return render(request,"opentamilapp/unigram.html")


def ngra(request):
    return render(request,"opentamilapp/ngram.html")


def sandhi_check(request):
    return render(request,"opentamilapp/sandhi_check.html")


def get_classify(request):
    return render(request,"opentamilapp/classifier.html")


def numstr(request, num):
    typ = request.GET.get("type")
    if isinstance(num,str) and num.find(".") == -1:
        num = int(num)
    else:
        num = float(num)
    if typ == "IN":
        out = tamil.numeral.num2tamilstr(num)
    else:
        out = tamil.numeral.num2tamilstr_american(num)
    data = {"result": out}
    json_string = json.dumps(data, ensure_ascii=False)
    # creating a Response object to set the content type and the encoding
    response = HttpResponse(json_string, content_type="application/json; charset=utf-8")
    return response

def unicod(request, tsci):
    cod = request.GET.get("cod")
    data = unicode_converter(tsci, cod)
    json_string = json.dumps(data, ensure_ascii=False)
    # creating a Response object to set the content type and the encoding
    response = HttpResponse(json_string, content_type="application/json; charset=utf-8")
    return response

def keech(request, k1):
    dic = {}
    for idx, kk in enumerate(k1.split(" ")):
        idx_len = len(get_letters(kk))
        # print('w# ',idx, idx_len )
        dic[idx] = idx_len
    json_string = json.dumps(dic, ensure_ascii=False)
    # creating a Response object to set the content type and the encoding
    response = HttpResponse(json_string, content_type="application/json; charset=utf-8")
    return response

@csrf_exempt
def call_sandhi_check(request):
    if request.method == "POST":
        k1 = html.escape(request.POST.get("tamiltext","சரியான உள்ளீடு கிடைக்கவில்லை"))
    else:
        k1 = html.escape(
            request.GET.get("tamiltext", "அங்குக் கண்டான் அந்த பையன் எத்தனை பழங்கள் ")
        )
    dic = {}
    temp = ""
    dic["old"] = k1
    text, res = check_sandhi(k1)
    for i, j in enumerate(k1.split()):
        try:
            if j != text[i]:
                text[i] = "<span class='highlight'>" + text[i] + "</span>"
        except IndexError:
            pass
    dic["new"] = " ".join(text)
    json_string = json.dumps(dic, ensure_ascii=False)
    # creating a Response object to set the content type and the encoding
    response = HttpResponse(json_string, content_type="application/json; charset=utf-8")
    return response

def translite(request, tan):
    tamil_tx = algorithm.Iterative.transliterate(azhagi.Transliteration.table, tan)
    data = {"result": tamil_tx}
    json_string = json.dumps(data, ensure_ascii=False)
    # creating a Response object to set the content type and the encoding
    response = HttpResponse(json_string, content_type="application/json; charset=utf-8")
    return response

def spell_check(request, k1):
    speller = Speller(lang="TA", mode="web")
    notok, suggs = speller.check_word_and_suggest(k1)
    json_string = json.dumps(suggs, ensure_ascii=False)
    # creating a Response object to set the content type and the encoding
    response = HttpResponse(json_string, content_type="application/json; charset=utf-8")
    return response

def test_ngram(request, ng):
    obj = DTrie()
    prev_letter = ""
    # per-line processor - remove spaces
    for char in get_letters("".join(re.split("\s+", ng)).lower()):
        if (prev_letter.isalpha() and char.isalpha()) or (
            utf8.is_tamil_unicode(prev_letter) and utf8.is_tamil_unicode(char)
        ):
            bigram = "".join([prev_letter, char])
            obj.add(bigram)  # update previous
        prev_letter = char
    actual = obj.getAllWordsAndCount()
    json_string = json.dumps(actual, ensure_ascii=False)
    # creating a Response object to set the content type and the encoding
    response = HttpResponse(json_string, content_type="application/json; charset=utf-8")
    return response

def anagram(request, word):
    AllTrueDictionary = wordutils.DictionaryWithPredicate(lambda x: True)
    TVU, TVU_size = DictionaryBuilder.create(TamilVU)
    length = len(utf8.get_letters(word))
    actual = list(wordutils.anagrams(word, TVU))
    json_string = json.dumps(actual, ensure_ascii=False)
    # creating a Response object to set the content type and the encoding
    response = HttpResponse(json_string, content_type="application/json; charset=utf-8")
    return response

def test_basic(request, word):
    n = request.GET.get("n")
    t = get_ngram_groups(word, int(n))
    json_string = json.dumps(t, ensure_ascii=False)
    # creating a Response object to set the content type and the encoding
    response = HttpResponse(json_string, content_type="application/json; charset=utf-8")
    return response

def revers(request, word):
    t = tamil.utf8.reverse_word(word)
    json_string = json.dumps(t, ensure_ascii=False)
    # creating a Response object to set the content type and the encoding
    response = HttpResponse(json_string, content_type="application/json; charset=utf-8")
    return response

def morse(request, direction="encode", word=""):
    if direction.lower().find("encode") >= 0:
        fn = tamilmorse.encode
    else:
        fn = tamilmorse.decode
    json_string = json.dumps(fn(word), ensure_ascii=False)
    print(json_string)
    response = HttpResponse(json_string, content_type="application/json; charset=utf-8")
    return response

# TBD:
# def sorttamil(request):

# TBD:
# def synthesize_number(request):

# TBD:
# def kalsee_on_web(request):


def tts_demo(request):
    if request.method == "GET":
        return render(request,"opentamilapp/tts_demo.html", {"solution": ""})
    assert request.method == "POST"
    words = request.POST.get("words", "")
    mp3path = os.path.join("static", "audio_%d.mp3" % random.randint(0, 1000000))
    static_path = os.path.join(os.path.split(__file__)[0], mp3path)
    tts = ConcatennativeTTS(words, static_path)
    tts.run()
    return render(request,"opentamilapp/tts_demo.html", {"solution": mp3path})


def xword(request):
    if request.method == "GET":
        return render(request,"opentamilapp/xword.html", {"solution": ""})
    assert request.method == "POST"
    words = request.POST.get("words", [])
    wordlist = list(filter(len, [w.strip() for w in re.split("\n+", words)]))
    grid, sol = generate_tamil_word_grid(wordlist)
    return render(
        request,
        "opentamilapp/xword.html",
        {"solution": grid, "wordlist": wordlist},
    )


def summarizer(request):
    if request.method == "GET":
        return render(
            request, "opentamilapp/summarizer.html", {"text_input": ""}
        )
    assert request.method == "POST"
    text_input = request.POST.get("text_input", "")

    # Create a SummaryTool object
    st = tamil.utils.SummaryTool()

    # Build the sentences dictionary
    sentences_dic = st.get_sentences_ranks(text_input)
    title = "தமிழ் பேசு.us:"
    # Build the summary with the sentences dictionary
    text_summary = st.get_summary(title, text_input, sentences_dic)
    in_w = len(tamil.utf8.get_words(text_input))
    out_w = len(tamil.utf8.get_words(text_summary))
    text_comments = (
        "உள்ளீடு அளவு: %d சொற்கள், வெளியீடு அளவு: %d சொற்கள். சுருக்கம் %3.3g.\n"
        % (in_w, out_w, in_w / (1.0 * out_w))
    )
    return render(
        request,
        "opentamilapp/summarizer.html",
        {
            "text_input": text_input,
            "text_summary": text_summary,
            "text_comments": text_comments
        },
    )

def classify_word(request):
    word = request.GET.get("tamiltext")
    result = process_word(word)
    data = {"result": result}
    json_string = json.dumps(data, ensure_ascii=False)
    # creating a Response object to set the content type and the encoding
    response = HttpResponse(json_string, content_type="application/json; charset=utf-8")
    return response

def minnal(request):
    return render(request,"opentamilapp/minnal.html", {})

def test_minnal(request, word):
    data, _ = tamil_minnal(re.split("\s+|,", word))
    json_string = json.dumps(data, ensure_ascii=False)
    # creating a Response object to set the content type and the encoding
    response = HttpResponse(json_string, content_type="application/json; charset=utf-8")
    return response

def load_textrandomizer_db():
    TEXTRANDOMIZER_DB = {}
    for jsonf in settings.TEXTRANDOMIZER_FILES:
        with codecs.open(
            os.path.join(os.path.dirname(__file__), "static", jsonf), "r", "utf-8"
        ) as fp:
            TEXTRANDOMIZER_DB[os.path.basename(jsonf)[0].upper()] = json.loads(
                fp.read()
            )

    return TEXTRANDOMIZER_DB


TEXTRANDOMIZER_DB = load_textrandomizer_db()


def textrandomizer(request, key=None):
    if not key or key != settings.APP_KEY:
        return Http404("Permission denied")
    request.session["authorized"] = key
    return render(request,"opentamilapp/textrandomizer.html")


def get_n_unique(n, r_range):
    rval = []
    assert n < len(r_range)
    while n > 0:
        rval.append(random.choice(r_range))
        n -= 1
        del r_range[r_range.index(rval[-1])]
    return rval


def test_textrandomizer(request, level):
    if request.session.get("authorized", "") != settings.APP_KEY:
        return Http404("Permission denied")
    if level == "kanigal":
        q, p, j = 6, 2, 2
        nilai = "கனிகள்"
        nilai_description = "இரண்டாம் நிலை"
    elif level == "malargal":
        nilai = "மலர்கள்"
        nilai_description = "முதல் எளிய நிலை"
        q, p, j = 10, 0, 0
    else:
        return Http404("எனக்கு இந்த நிலை தெரியவில்லை - %s" % (level))
    assert (q + p + j) == 10
    nq = get_n_unique(q, list(range(0, len(TEXTRANDOMIZER_DB["Q"]))))
    np = get_n_unique(p, list(range(0, len(TEXTRANDOMIZER_DB["P"]))))
    nj = get_n_unique(j, list(range(0, len(TEXTRANDOMIZER_DB["J"]))))
    questions = []
    answers = []
    QK = list(TEXTRANDOMIZER_DB["Q"].keys())
    QV = [TEXTRANDOMIZER_DB["Q"][k] for k in QK]
    PK = list(TEXTRANDOMIZER_DB["P"].keys())
    PV = [TEXTRANDOMIZER_DB["P"][k] for k in PK]
    JK = list(TEXTRANDOMIZER_DB["J"].keys())
    JV = [TEXTRANDOMIZER_DB["J"][k] for k in JK]
    for idq in nq:
        questions.append(QK[idq] + " ?")
        answers.append(QV[idq])
    for idp in np:
        questions.append(PK[idp] + " ?")
        answers.append(PV[idp])
    for idj in nj:
        questions.append(JK[idj] + " ")
        answers.append(JV[idj])
    assert len(questions) == (q + p + j)
    return render(
        request,
        "opentamilapp/textrandomizer.html",
        {
            "questions": list(zip(questions, answers)),
            "nilai": nilai,
            "nilai_description": nilai_description,
        },
    )


def tastemmer(request, use_json=False):
    if request.method == "GET":
        return render(request,"opentamilapp/stemmer.html", {"text_output": ""})
    assert request.method == "POST"
    text_input = request.POST.get("text_input", "")
    words_in = list(filter(len, re.split("\s+", text_input)))
    words_out = TamilStemmer().stemWords(words_in)
    data = list(zip(words_in, words_out))
    if use_json:
        json_string = json.dumps(data, ensure_ascii=False)
        response = HttpResponse(
            json_string, content_type="application/json; charset=utf-8"
        )
    return render(
        request, "opentamilapp/stemmer.html", {"text_output": data, "text_input": text_input}
    )

@csrf_exempt
def tamil_date(request):
    n = datetime.now()
    default = True
    if request.method == 'POST':
        default = False
        value = request.POST.get("meeting-time")
        if value:
            n = dateutil_parser.parse(value)
    d = ta_datetime(n.year, n.month, n.day, n.hour, n.minute)
    tamil_date = d.strftime_ta("%a %d, %b %Y")
    tamil_time = d.strftime_ta("%A (%d %b %Y) %p %I:%M")
    return render(request,"opentamilapp/date.html",{"date":tamil_date,
                                       "time":tamil_time,
                                       "time_now":n.ctime(),
                                       "default":default
                                       })

def tamil_calculator(request):
    default = True
    n = 0
    as_tamil = ""
    value =  "ஓர் ஆயிரம் கழித்தல் ஐந்து பெருக்கல் ( ஒன்பது கூட்டல் ஒன்று )"
    mp3path = None
    if request.method == 'POST':
        default = False
        value = request.POST.get("kanippaan-varigal")
        n = kanakkidu(value)
        as_tamil = tamil.numeral.num2tamilstr_american(n)

        mp3path = os.path.join("static", "calculator_audio_%d.mp3" % random.randint(0, 1000000))
        static_path = os.path.join(os.path.split(__file__)[0], mp3path)
        tts = ConcatennativeTTS(f"உங்கள் கேள்வியான, {value} இன் விடை, {as_tamil}", static_path)
        tts.run()

    return render(request,"opentamilapp/calculator.html",
                  {"og_value":value,
                   "n":n,
                   "tamil_result":as_tamil,
                   "has_result":not default,
                   "solution": mp3path,
                   })

def tamil_adhikaram_detail(request,num):
    assert num >= 1 and num <= 133, "only 133 adhikarams are allowed"
    pass

def tamil_paal_detail(request,num):
    assert num >= 1 and num <= 3, "only 3 paal categories are allowed"
    adhikarangal = get_pals()
    paal = list(adhikarangal.keys())[num-1]
    return render(request, "opentamilapp/kural.html", {"paal":paal,
                                                       "adhikaram": {paal:adhikarangal[paal]}})

def tamil_kural_detail(request,num):
    if num == 0:
        num = int(request.POST.get("kuralID",1))
    assert num >= 1 and num <= 1330, "only 1330 kurals are known"
    kural = kurals()[num-1]
    adi1, adi2 = kural.row1, kural.row2
    seeradi1, seeradi2 = சீர்_பிரித்த_குறள்( num )
    venba_parsed: Venba = yappu_venba(kural.ta)
    as_li = lambda x: f'<li>{str(x)}</li>'
    venba1 = "\n".join(map(as_li,venba_parsed.adi_list[0].seer_list))
    venba2 = "\n".join(map(as_li, venba_parsed.eetradi.seer_list))

    mp3path = os.path.join("static", "audio_kural_%d.mp3" % random.randint(0, 1000000))
    static_path = os.path.join(os.path.split(__file__)[0], mp3path)
    words = (seeradi1 +' '+ seeradi2).replace('-',' ')
    #words = kural.ta
    tts = ConcatennativeTTS(words, static_path)
    tts.run()
    return render(request, "opentamilapp/kural_detail.html",
                  {
                      "kural":kural,
                      "kuralrow1":adi1,
                      "kuralrow2":adi2,
                      "seeradi1":seeradi1,
                      "seeradi2":seeradi2,
                      "venba1":venba1,
                      "venba2":venba2,
                      "audiopath":mp3path,
                  })


def tamil_kural(request):
    return render(request,"opentamilapp/kural.html",{"adhikaram":get_adhikaram()})

def tamil_kuralgen(request):
    if request.method == 'POST':
        prompt = request.POST.get("prompt")
        row1,row2 = get_matching_kural(prompt)
        return render(request,"opentamilapp/kuralgen.html",{
            "kuralrow1":row1,
            "kuralrow2":row2
        })
    return render(request,"opentamilapp/kuralgen.html",{})
