from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__) 
# print(__name__) # __main__


@app.route("/")
def my_home():
    # print( url_for('static', filename='favicon.ico'))
    return render_template('./index.html')

# @app.route("/about.html")
# def about_me():
#     return render_template('./about.html')

# @app.route("/works.html")
# def works():
#     return render_template('./works.html')

# @app.route("/contact.html")
# def contact():
#     return render_template('./contact.html')

@app.route('/<string:page_name>') # Routes pages dynamically 
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database: # opens database file and sets mode to append, to add email, subject, and message input into form on webpage
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email}, {subject}, {message}') # sets file to the database file and writes the parameters above

def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2: # newline allows for each entry to be appended on a new line
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',',  quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict() # Grabs input form data as a dictionary and sets it to data variable
            write_to_file(data) # Writes form data to database.txt
            write_to_csv(data) # Writes form data to database.csv
            return redirect('/thankyou.html') # Redirects page to thankyou.html if request method is post
        except:
            return 'did not save to databse'
    else:
        return 'something went wrong.'
