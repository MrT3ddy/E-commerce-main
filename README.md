# E-commerce

# OVERVIEW
Using Python and Flask this is a website I am creating for my friend to use for his clothing brand,
it will allow him to sell clothes and use CRUD operations to update his inventory securely.
Front end will be the last task.


Main Resource:
  - Flask Documentation
  
What I have so far
- Authentication for admin user added through the database
- Listing of every product from the database for home page 
- Product page that dynamically produces data based on id of product
- Crud operation for Admin side (create, update, delete products and all their info)
- Shopping Cart that uses cookies, no need to be logged in as a user


Planning to use:
- square API
- AWS EC2
- CSS/HTML


  

# After downloading cloan
https://flask.palletsprojects.com/en/2.0.x/installation/#optional-dependencies


0.) In CLI for your operating system go to the top directory of 'wbp copy' : aka cd 'wbp copy'

1.) Activate environment

. venv/bin/activate



 
2.) Activate project folder (ecommerce)(not e-commerce)

$ export FLASK_APP=ecommerce

$ export FLASK_ENV=development

$ flask init-db

$ flask run

3. ) Access the site with the provided IP address in the terminal



