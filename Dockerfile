FROM python:3.9

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

# Upgrade pip
RUN pip install --upgrade pip

# Install the requirements.
RUN pip install -r requirements.txt

# Copy the rest of the code.
COPY . /app/

RUN python /app/manage.py migrate
EXPOSE 5000
ENTRYPOINT ["python","/app/manage.py","runserver","0.0.0.0:5000"]
