# E-commerce

# OVERVIEW
Using Python and Flask this is a website I am creating for my friend to use for his clothing brand,
it will allow him to sell clothes and use CRUD operations to update his inventory through a secure end point.

Main Resource:
  - Flask Documentation
  
What I have so far
- Authentication for admin user added through the database
- Listing of every product from the database for home page 
- Product page that dynamically produces data based on key of the previous action

What I need Step by Step (difficulty & time consumption)
- Crud operation for Admin side (easy) (security will be new)
- Cart functionality using sessions (cookies) (medium)
- Add images to product listing in the database (easy)
- Update the database to make it more efficient (medium)
- Adapt square API into this 'system' (medium/hard)
- Add more error handeling. (medium)
- Add more security for authentication (hashing), sessions (cart), ect (medium)
- Deploy on AWS EC2 (easy)
- Work on front end last (medium)

(So far) How the cart will work-
Going to use sessions import in flask to keep cart information in the clients cookies without authentication.

  I might end up stopping this project and starting something new at some point in time because I have learned what I needed to learn from starting this project, I would love to continue it but I hate to reinvent the wheel where in this case we could just use shopify.  Although starting this project resparked my interest in creating through use of resources alone. I enjoyed learning Flask from the ground up with this project and I am ready to move on to Django.
  



# HOW TO START PROJECT
https://flask.palletsprojects.com/en/2.0.x/installation/#optional-dependencies

1.)Add necessary folders

In the e-commerce folder run in terminal/cmd (not inside the ecommerce)

$ mkdir myproject

$ cd myproject

$ python3 -m venv venv


2.) Activate environment

. venv/bin/activate


3.) Install Flask

$ pip install Flask

(update flask)

 
4.) Activate project folder (ecommerce)(not e-commerce)

$ export FLASK_APP=ecommerce

$ export FLASK_ENV=development

$ flask init-db

$ flask run



