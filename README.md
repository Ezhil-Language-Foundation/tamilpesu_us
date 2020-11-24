Open Tamil Web Interface

sudo pip install -r requirements.txt

git clone https://github.com/abuvanth/open-tamil-web-interface.git

cd open-tamil-web-interface

python manage.py runserver

##### On Docker
1. Build and run the app
    ```shell script
    docker build . -t tamilpesu
    docker run -d -p 5000:5000 tamilpesu
    ```
2. Open `http://localhost:5000` on your browser.
