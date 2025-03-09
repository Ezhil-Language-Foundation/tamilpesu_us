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

# Running Locally using Docker
You need to have a Docker installed on local machine. Then you have to build the docker image for this repository using the commands:
(note: replace "my-image-name" with your suitable name; its just meta-syntactic variables [மேல்தொடரியல் மாறி])
```
$ docker build -t my-image-name
```

```
$ docker run -p 8080:5000 -it my-image-name
```

Then open your browser at localhost 8080 you should see,
<img width="1303" alt="image" src="https://github.com/user-attachments/assets/09b9f2ae-534b-4208-ba71-7cf99aa20b5b" />
