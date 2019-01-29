# CSV BROWSER

CSV Browser is the webapp to browse and display data from csv files. It will store the data in the database with the JSON format with the help of Python functions that can filter the data by the given fields.

Technologies used:
  - Python/ Django framework
  - MongoDB 
  

## Installation Instructions
  1. clone the project
  `git clone https://github.com/khatryshikha/csv_browser_project.git`
  2. cd to project folder `cd csv_browser_project` and create virtual environment
  `virtualenv venv`
  3. activate virtual environment
  `source venv/bin/activate`
  4. install requirements
  `pip install -r requirements.txt`
  5. run the server
  `python manage.py runserver`

  This prjoect is also hosted on heroku using Mlab DaaS : http://demo-csvbrowser.herokuapp.com/

  ** To test this, CSV data file is also available here as `data.csv`.