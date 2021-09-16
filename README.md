<h1 align="center">BANFF National Park Hike Booker</h1>

[View the live project here](to be written)

Project Goal and into here - to be written
project is banffnp and app is hikebooker

![Mockup](to be written)

## Index – Table of Contents
* [User Experience (UX)](#user-experience-ux) 
* [Features](#features)
* [Design](#design)
* [Planning](#planning)
* [Technologies Used](#technologies-used)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)

## User Experience (UX)

-   ### User stories :

* US01 to be written
* US02 to be written
* US03 to be written   . ... etc

## Features

### Existing Features

-   __F01 to be written__
    - to be written - blah de blah

      ![to be writen](to be written)

### Features which could be implemented in the future

- __to be written__
    - Cto be written

## Design

-   ### Typography, Imagery and Colour Scheme
    - to be written

-   ### Wireframes

    <details>
    <summary>Desktop Wireframes</summary>

    ![Desktop Wireframes](to be written)
    </details>
    <details>
    <summary>Tablet Wireframes</summary>

    ![Desktop Wireframes](to be written)
    </details>
    <details>
    <summary>Smartphone Wireframes</summary>

    ![Desktop Wireframes](to be written)
    </details>

-   ### Entity-Relationship diagrams for DBMS
    
    <details>
    <summary>ER Diagrams</summary>

    ![ER Diagrams](to be written)
    </details>

## Planning

### to be written - include information and links here re agile process used

## Technologies Used

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [Javascript](https://en.wikipedia.org/wiki/JavaScript)
-   [to be written](to be written)

### Frameworks, Libraries & Programs Used

-   [Google Fonts:](https://fonts.google.com/) to be written ??????????????????
-   [Font Awesome:](https://fontawesome.com/) was used to add icons for aesthetic and UX purposes.
-   [Git:](https://git-scm.com/) was used for version control by utilising the Gitpod terminal to commit to Git and Push to GitHub.
-   [GitHub:](https://github.com/) is used as the respository for the projects code after being pushed from Git.  
-   [GitHub:](https://github.com/) to be written re agile ?????????????
-   [dbdiagram.io](https://dbdiagram.io/home) was used to create the Entity Relationship diagrams for the application data model
-   [Balsamiq:](https://balsamiq.com/) was used to create the wireframes during the design process.
-   [Django](https://www.djangoproject.com/) used as the framework to support rapid and secure development of the application
-   [Gunicorn](https://gunicorn.org/) used as the Web Server to run Django on Heroku
-   [dj_database_url](https://pypi.org/project/dj-database-url/) library to allow use database urls to connect to the postgres db
-   [psycopg2](https://pypi.org/project/psycopg2/) database adapter to support the connection to the postgres db
-   [Cloudinary](https://cloudinary.com/) used to store the images used by the application
-   [Summernote](https://pypi.org/project/django-summernote/) used to provide WYSIWYG editing on the Hike editing screen

## Testing

### Validator Testing 

- [HTML Validator](https://validator.w3.org/)

    - to be written
      ![to be written](to be written)
  

- [CSS Validator](https://jigsaw.w3.org/css-validator/)

    - to be written 
      ![to be written](to be written)


- [Javascript Validator](https://jshint.com/)

    - to be written 
      ![to be written](to be written)

### Automated Testing

   - to be written 
      ![to be written](to be written)

### Browser Compatibility

- Testing has been carried out on the following browsers :
    - to be written
 
    
### Manual Testing Test Cases and Results

- The below table details the test cases that were used, the results and a cross-reference to the Feature ID that each test case exercised (click to open image).  The test cases are primarily based on the User Story acceptance criteria that we used to test iterations of the code during development.

  <details>
    <summary>Test Cases</summary>

    ![Test Cases](to be written)
  </details>
  

### Known bugs

- to be written

## Deployment

to be written blah blah  - don't forget to mention DEBUG

check for errors
check for commented out code
do I need to test settings.py

1. Create application and Postgres DB on Heroku
2. Create Postgres DB and link on app on Heroku
3. Configure environment variables

### How to clone the repository 

- Go to the https://github.com/elainebroche-dev/pf4-guided-hike-booker repository on GitHub 
- Click the "Code" button to the right of the screen, click HTTPs and copy the link there
- Open a GitBash terminal and navigate to the directory where you want to locate the clone
- On the command line, type "git clone" then paste in the copied url and press the Enter key to begin the clone process
- Changes made to the local clone can be pushed back to the repository using the following commands :

  - git add *filenames*  (or "." to add all changed files)
  - git commit -m *"text message describing changes"*
  - git push

- N.B. Any changes pushed to the master branch will take effect on the live project

### Create Application and Postgres DB on Heroku
- Log in to Heroku at https://heroku.com - create an account if needed.
- From the Heroku dashboard, click the Create new app button.  For a new account an icon will be visible on screen to allow you to Create an app, otherwise a link to this function is located under the New dropdown menu at the top right of the screen.
- On the Create New App page, enter a unique name for the application and select region.  Then click Create app.
- On the Application Configuration page for the new app, click on the Resources tab.
- In the Add-ons search bar enter "Postgres" and select "Heroku Postgres" from the list - click the "Submit Order Form" button on the pop-up dialog.
- Next click on Settings on the Application Configuration page and click on the "Reveal Config Vars" button - check the DATABASE_URL has been automatically set up. 
- Add a new Config Var called SECRET_KEY and assign it a value - any random string of letters, digits and symbols.
- The settings.py file should be updated to use the DATABASE_URL and SECRET_KEY environment variable values as follows :

  - DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}

  - SECRET_KEY = os.environ.get('SECRET_KEY')

- In Gitpod, in the project terminal window, run the command : python3 manage.py migrate to initialize the data model in postgres database.
- Make sure the project requirements.txt file is up to date with all necessary supporting files by entering the command : pip3 freeze --local > requirements.txt
- Commit and push any local changes to GitHub.

### Configure Cloudinary to host images used by the application
- Log in to Cloudinary - create an account if needed.  To create the account provide your name, email and setup a password.  For "primary interest" you can choose "Programmable Media for image and video API".  Click "Create Account" and you will be sent an email to verify your account and bring you to the dashboard.
- From the dashboard, copy the "API Environment variable" value by clicking on the "Copy to clipboard" link.
- Log in to Heroku and go to the Application Configuration page for the application.  Click on Settings and click on the "Reveal Config Vars" button.
- Add a new Config Var called CLOUDINARY_URL and assign it the value copied from the Cloudinary dashboard, but remove the "CLOUDINARY_URL=" at the beginning of the string. 

### Connect the Heroku app to the GitHub repository
- Go to the Application Configuration page for the application on Heroku and click on the Deploy tab.
- Select GitHub as the Deployment Method and if prompted, confirm that you want to connect to GitHub. Enter the name of the github repository (the one used for this project is (https://github.com/elainebroche-dev/pf4-guided-hike-booker) and click on Connect to link up the Heroku app to the GitHub repository code.
- Scroll down the page and choose to either Automatically Deploy each time changes are pushed to GitHub, or Manually deploy - for this project Automatic Deploy was selected.
- The application can be run from the Application Configuration page by clicking on the Open App button.
- The live link for this project is (https://banffnp.herokuapp.com/)



### Create Postgres DB 
- While still logg

  The live link can be found here - [to be written](to be written) 


 
## Credits 


  

### Code 
constraints https://docs.djangoproject.com/en/3.2/ref/models/constraints/
error when a foreign key field was included in search field list https://stackoverflow.com/questions/11754877/troubleshooting-related-field-has-invalid-lookup-icontains
checks for capacity : https://stackoverflow.com/questions/65416042/max-and-min-values-for-a-django-model-field-according-to-the-values-already-int
talk about the 2 walkthroughs - specifically for testing and for basic html and css structures  https://github.com/Code-Institute-Solutions/django-blog-starter-files/tree/master/templates
round decimal field to 2 places https://stackoverflow.com/questions/37958130/automatically-round-djangos-decimalfield-according-to-the-max-digits-and-decima
information on jumbotron images
https://stackoverflow.com/questions/22000754/responsive-bootstrap-jumbotron-background-image
- code on how to removed trailing zeroes from decimal fields - normalize function - https://stackoverflow.com/questions/40135464/django-remove-trailing-zeroes-for-a-decimal-in-a-template

### Configuration and Deployment
- The Code Institute "Django Blog Cheat Sheet" was used extensively to install and configure frameworks and libraries, set up the dbms and prepare the application for deployment : [CI Cheat Sheet](https://codeinstitute.s3.amazonaws.com/fst/Django%20Blog%20Cheat%20Sheet%20v1.pdf)

### Content 
- Information on individual hikes was found on the Government of Canada - Parks Canada website : [Parks Canada](https://www.pc.gc.ca/en/pn-np/ab/banff/activ/randonee-hiking)

### Media 
- The fonts used were imported from [Google Fonts](https://fonts.google.com/)
- to be written [Font Awesome](https://fontawesome.com/)
- to be written
- The favicon was created from the "exchange" icon image on [Font Awesome](https://fontawesome.com/) ???????????????????  to be written ??????????????
- ??? default hike image - boot crossing stream - Photo by <a href="https://unsplash.com/@sickhews?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Wes Hicks</a> on <a href="https://unsplash.com/s/photos/hiking-boots?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
- jumbotron background - woman on boulder - Photo by <a href="https://unsplash.com/@stephenleo1982?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Stephen Leonardi</a> on <a href="https://unsplash.com/s/photos/hiking?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
  
  

### Acknowledgments

- to be written