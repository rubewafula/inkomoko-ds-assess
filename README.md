# inkomoko-ds-assess
Inkomoko Data Science Assessmento

This assessement is done with Flask, Flask-restful framework.


I have registered the below endpoints
    '/vx/extract-data' - Hand data extraction and saving to database
    '/vx/accept/data' - Accept data submission via web hook
    '/vx/register/webhook' - Handle registration of webhook to inkmoko

Structure
   .configs.ini - Configuration file, database, other configs
   main.py - Entry point, create the Fask app and acts as the entry point

   DataAssignment.py -  Has endpoints to handle the actual post for all API 
       endpoints

   Models.py - Models mapped to Database tables using sqlalchemny ORM implementations

   Db.py - Handles database logic for creation of specific data creation login

   inkomoko.wsi - Register wasgi application of production deployment via uwsgi container
   
   uwsgi.ini -  Configurations for uwsgi deployment

   Migrations Folder - Has database migrations that can be managed via alembic
     - Migrations can be deployed by including alembic config file alembic.ini in route dir
     - Managing database connection and deploying the migrations

   sql - Folder has actual dump of raw sql database
      - This assigment has been done with mysql database

   sys - Folder has deployment script for deployment via nginx with uwsgi container

   requirements.txt - Python requirements. Need to be installed via pip in virtual environment 
    - There are liraries and modules we have used in the delopment and are required to run the application


Deployment
    Pythn 3.9
    nginx
    uwsgi

    The nginx config file is available in the sys/nginx.conf
    The service file is available in sys/inkomoko.servie to be copied to
    /etc/systemd/system/ and deployed as service, the paths in this file point to
    the project dir and need to be validated for actual deployment

    The application handles logging via syslog - The requirement is to adjust logging params in uwsgi.ini in root dir



Live 

   This application is hosted and is avaliable on this public URL
   http://130.211.86.77:9000/vx/accept/data


