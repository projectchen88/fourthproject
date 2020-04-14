# PROJECT 3 : COOKED FOOD E-COMMERCE WEBSITE

### Objective :   
    To build a E-commerce website to allow user to register and login and buy food from different stalls. 
    User will be able to buy and sell their own dishes.   
    
#### SCOPE
The website allows User to :
    
    * Allow User to register for new account and login 
    * CREATE / READ / UPATE / DELETE a dish for sale
    
#### Demo
A live demo can be found here. https://foodecomm.herokuapp.com/

#### UX
    My Considerations for the website:
    * user able to submit, make changes and remove a dish for sale on the website
    * easy for user to navigate and simple to read the details
    * user can only edit their own listing
    * user can only make changes to listing if they are login
    * will re-route to let user sign in if they tried to submit dish
    * user can make payment using the credit card payment

#### Technologies
    1. HTML
    2. CSS 
    3. Bootstrap 
    4. Jinja
    5. Python
    6. Whitenoise 
    7. PostgreSQL
    8. Django 

#### Features
				
**My Design of the site :**

    * Easy for user to navigate and buy and sell their dishes
    
    Limitations: 
    * no search function at the moment due to time limitation
    * Social media links not link not set up

#### Testing
Manual Testing is done to ensure that the all functions are functional.
Test Results as follows :

*No* | *Steps* | *Expected Results* | *Observations*
--- | --- | --- | ---
1a | `On the Landing Page, click on the "Submit new dish" in navbar`| `Link to the submission of new dish page (if login), else route to login page`| **Pass** 
1b | `Enter the details in form and submit`|`Render successful submission page with success message passed over to show login` | **Pass** 
2a | `Click on the checkout of the dish`|`display the full breakdown of the dish pricing and pay button` | **Pass** 
2a | `Click on the paynow button`|`route to paypal default payment form` | **Pass** 
3 | `In 'Admin Page', Click "Edit" link on right of each line`|`Show form with details of selected dish and allow user to enter new info or upload new image` | **Pass** 
4 | `In 'Admin page' Click "Delete" link on top right of each line`|`Render page to check with user if the removal of the selected dish is final` | **Pass** 
4b | `Click "Remove from shelf`|`Remove from database and return to admin page` | **Pass** 

#### Deployment
This site is hosted using Heroku App Link : 
_https://foodecomm.herokuapp.com/_

    All codes are uploaded to GitHub and links are made to Heroku by installing in bash terminal in projects.
    Regular commits are push to the Github subsequently push to heroku to deploy.
    .gitignore file is added to remove files that are not required or files that we do not wish to be uploaded to Github

_Deploy Heroku:_

    i) Install Heroku using bash
    ii) Login to Heroku
    iii) Install gunicorn
    iv) Create Procfile and requirements.txt
    V) Commit and push to Heroku 
    vi) Set up the Environment Vasriables
    vii) Update Dependencies


#### Credits
    Uses W3School for many reference (https://www.w3schools.com/)
    Uses fontawesome for the social media icons (https://fontawesome.com/)
    Uses Bootstrap for templates (https://getbootstrap.com/)

 