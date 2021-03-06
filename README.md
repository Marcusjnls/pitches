# [PitchR](https://pitches-markozy.herokuapp.com/)

## PitchR is a web application that is meant for users to add pitches on different categories
### September 18th, 2019
#### By **[Marcus Jean-Louis](https://github.com/marcusjnls)**

## Description
The PitchR web application is meant for users to post pitches on any of the 7 different categories. These categories are:

    1. Interview Pitches
    2. Product Pitches
    3. Promotion Pitches
    4. Business Pitches
    5. Academic
    6. Political
    7. Technology
    8. Health

A user can select any of the categories from the navbar to view the pitches on these categories

Other users can give feedback to the pitch posts by commenting, liking or disliking the pitch. 

## Specifications
Get the specs [here](https://github.com/devwaweru/PitchIt/blob/master/SPECS.md)

## Set-up and Installation

### Prerequiites
    - Python 3.6
    - Ubuntu software

### Clone the Repo
Run the following command on the terminal:
`git clone https://github.com/Marcusjnls/pitch.git && cd PitchIt`

Install [Postgres](https://www.postgresql.org/download/)

### Create a Virtual Environment
Run the following commands in the same terminal:
`sudo apt-get install python3.6-venv`
`python3.6 -m venv virtual`
`source virtual/bin/activate`

### Install dependancies
Install dependancies that will create an environment for the app to run
`pip3 install -r requirements`

### Prepare environment variables
```bash
export DATABASE_URL='postgresql+psycopg2://username:password@localhost/pitchit'
export SECRET_KEY='Your secret key'
```

### Run Database Migrations
```
python manage.py db init
python manage.py db migrate -m "initial migration"
python manage.py db upgrade
```

### Running the app in development
In the same terminal type:
`python3 manage.py server`

Open the browser on `http://localhost:5000/`

## Known bugs

1. A user can be registered but an error displays after, please use the same credentials used in the registration process to log in.
2. The reset password functionality is a bit buggy but will be fixed.

## Technologies used
    - Python 3.6
    - HTML
    - Bootstrap 4
    - JavaScript
    - Heroku
    - Postgresql

## Support and contact details
Contact me for any comments, reviews or advice;
Name: Marcus Jean-Louis
Phone: 0722-894999
Email: marcusjnls@gmail.com

### License
Copyright (c) **Marcus Jean-Louis**