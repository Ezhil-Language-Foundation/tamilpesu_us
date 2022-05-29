FROM ubuntu:latest

# These two environment variables prevent __pycache__/ files.
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Make a new directory to put our code in.
RUN mkdir /app

# Change the working directory.
# Every command after this will be run from the /app directory.
WORKDIR /app

# Copy the requirements.txt file.
COPY ./requirements.txt /app/

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip
# Upgrade pip
RUN pip install --upgrade pip

# Install the requirements.
RUN pip install -r requirements.txt
RUN apt-get install -y aspell aspell-ta


# Copy the rest of the code.
COPY . /app/

# Prepare Staticfiles and Database
RUN python /app/manage.py collectstatic --no-input
RUN python /app/manage.py migrate --no-input

# Serve
EXPOSE 5000
ENTRYPOINT ["python","/app/manage.py","runserver","0.0.0.0:5000"]
