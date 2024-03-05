"""opentamilweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import sys
from django.shortcuts import redirect
from django.urls import path, re_path
from .views import *

urlpatterns = [
    path("", index, name="home"),
    path("apidoc/", lambda r: redirect("/static/sphinx_doc/_build/html/index.html")),
    path("tts_demo/", tts_demo, name="tts_demo"),
    path("translite/", trans, name="translite"),
    path("tsci/", uni, name="tsci"),
    path("keechu/", keechu, name="keechu"),
    path("sandhi-check/", sandhi_check, name="sandhi"),
    path("spell/", spl, name="spell"),
    path("revers/", rev, name="rever"),
    path("number/", num, name="number"),
    path("anagram/", anag, name="anagram"),
    path("unigram/", unig, name="unigram"),
    path("vaypaadu/", vaypaadu, name="multiplication"),
    path("number/<int:num>/", numstr, name="numstr"),
    re_path(r"^tsci/(?P<tsci>.+?)/$", unicod, name="unicod"),
    re_path(r"^keechu/(?P<k1>.+?)/$", keech, name="keech"),
    path("sandhi-checker/", call_sandhi_check, name="sandhi_check"),
    re_path(r"^translite/(?P<tan>.+?)/$", translite, name="phonetic"),
    re_path(r"^spell/(?P<k1>.+?)/$", spell_check, name="spell_check"),
    path("aspell/", aspell_spell_check, name="aspell_spell_check"),
    re_path(r"^aspell_spellchecker",aspell_spellchecker,name="aspell_spellchecker"),
    path("tamilinayavaani/", tamilinayavaani_spell_check, name="tamilinayavaani_spell_check"),
    re_path(r"^tamilinayavaani_spellchecker",tamilinayavaani_spellchecker,name="tamilinayavaani_spellchecker"),
    path("ngram/", ngra, name="ta_ngram"),
    re_path(r"^ngram/(?P<ng>.+?)/$", test_ngram, name="ngram"),
    re_path(r"^anagram/(?P<word>.+?)/$", anagram, name="ta_anagram"),
    re_path(r"^unigram/(?P<word>.+?)/$", test_basic, name="ta_unigram"),
    re_path(r"^revers/(?P<word>.+?)/$", revers, name="ta_revers"),
    path("xword/", xword, name="ta_xword"),
    re_path(r"^summarizer/", summarizer, name="ta_summarizer"),
    path("morse/<path:direction>/<path:word>/", morse, name="ta_morse"),
    path("morse/", morse_code, name="morse_code"),
    path("minnal/", minnal, name="ta_minnal"),
    re_path(r"^minnal/(?P<word>.+?)/$", test_minnal, name="minnal"),
    path(
        "textrandomizer_auth/<path:key>/", textrandomizer, name="ta_textrandomizer"
    ),
    path("textrandomizer/<path:level>/", test_textrandomizer, name="textrandomizer"),
    path("stemmer/", tastemmer, name="stemmer"),
    path("stemmer/json/", lambda x: tastemmer(x, use_json=True), name="json_stemmer"),
    re_path(r"version/",version,name="version"),
    path("classify-word/", classify_word, name="classify_word"),
    path("get-classify/", get_classify, name="classifier"),
    path("date/",tamil_date,name="tamil_date"),
    path("calculator/",tamil_calculator,name="tamil_calculator"),
    path("kuralgen/", tamil_kuralgen, name="tamil_kuralgen"),
    path("kural/", tamil_kural, name="tamil_kural"),
    path("kural/detail/<int:num>/", tamil_kural_detail, name="tamil_kural_detail"),
    path("kural/paal/detail/<int:num>/", tamil_paal_detail, name="tamil_paal_detail"),
    path("kural/adhikaram/detail/<int:num>/", tamil_adhikaram_detail, name="tamil_adhikaram_detail"),
]
