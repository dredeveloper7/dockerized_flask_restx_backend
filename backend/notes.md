This repo is an example template for a flask restx backend with user model for flask sqlalchemy and namespace used for a collection of apis, currently 1 api created for authentication'

1) !!! First things first - create a virtual env using your preferred module within the main project folder
using the requirements.txt install the requirement packages 

To spin up server use:
1) Flask run - or
2) Flask run --port XXXX

Reading material

https://flask-restx.readthedocs.io/en/latest/scaling.html

- How namespace (Restx api componentisation) compares to blueprints.
- Blueprints are essential geenric componentisation of flask applications where different section of the apps are split into different directories in structures called blueprints. - akin to django apps.
- Namespace are used specifically to split up apis.

https://www.digitalocean.com/community/tutorials/how-to-structure-a-large-flask-application-with-flask-blueprints-and-flask-sqlalchemy


Understanding flask-sqlalchemy and using flask migrate to automate updates of relation db
https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/quickstart/
https://flask-migrate.readthedocs.io/en/latest/

To initialse the db in this project use: 
- flask db init
- this will create an instance folder in the main app package and a migrations folder for db upgrades.
then for changes to models that represent db tables you must use
1) flask db migrate and 
2) flask db upgrade

Remember that the simple sqlite db thats created locally is very limited and you often can't alter tables once made.
For a more robust build - you might need to download postgres and configure the db in config.py to link to that
or any other web based test db.






https://blog.miguelgrinberg.com/post/fixing-alter-table-errors-with-flask-migrate-and-sqlite
