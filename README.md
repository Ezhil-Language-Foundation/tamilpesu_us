# Web Interface for Tamil Open-Source Software (TOSS)
Various Tamil Open-Source projects are hosted using this repository,

1. Open-Tamil <https://github.com/Ezhil-Language-Foundation/open-tamil/>
2. Tamil Sandhi Checker <https://github.com/nithyadurai87/tamil-sandhi-checker>
3. Tamil InayaVaani Checker <https://github.com/tshrinivasan/Tamilinaiya-Spellchecker/>
4. Tamil TTS <https://github.com/vasurenganathan/tamil-tts>
5. Kural-Gen <https://github.com/MannarAmuthan/kural-gen>

# Installation / Local Run

git clone https://github.com/Ezhil-Language-Foundation/open-tamil.git

cd open-tamil/webapp

sudo pip install -r requirements.txt

python manage.py compilemessages

python manage.py runserver

# for tamil translation of website

add to template {% trans "this is example" %}

then put - python manage.py makemessages -l "ta"

edit translation file

open-tamil/webapp/locale/ta/LC_MESSAGES/django.po


msgid "this is example"

msgstr "இது எடுத்துக்காட்டு"

then put following commands

python manage.py compilemessages

python manage.py runserver

