from flask import Flask, render_template
import csv

application = app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
# @app.route('/codeblog')
# def listing():
#     projects = []
#     with open('static/projects.csv', newline='') as csvfile:
#        reader = csv.DictReader(csvfile)
#        for row in reader:
#            if row["imgurl"] == "default":
#                projects.append([row["title"],row["posturl"],"https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/3f007d62-f058-4a75-b8bc-ebad34e9b0cf/dbfz5hz-3d41cf4a-bd40-4289-8eac-a5289f2addb4.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOiIsImlzcyI6InVybjphcHA6Iiwib2JqIjpbW3sicGF0aCI6IlwvZlwvM2YwMDdkNjItZjA1OC00YTc1LWI4YmMtZWJhZDM0ZTliMGNmXC9kYmZ6NWh6LTNkNDFjZjRhLWJkNDAtNDI4OS04ZWFjLWE1Mjg5ZjJhZGRiNC5wbmcifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6ZmlsZS5kb3dubG9hZCJdfQ.bE-ImmLksEbxjEqtH9sfYs_UmLOe2m35ss1nxHmnUFI",row["date"],row["text"]])
#            else:
#                projects.append([row["title"],row["posturl"],row["imgurl"],row["date"],row["text"]])
#     return render_template('projects.html', posts=projects)
