from flask import Flask, render_template, redirect, request, flash
import csv
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os
from datetime import datetime
import secrets



load_dotenv()


app = Flask('__name__')
app.secret_key = os.environ.get('FLASK_SECRET_KEY', secrets.token_hex(16))     

secret_key = secrets.token_hex(16)
os.environ['FLASK_SECRET_KEY'] = secret_key



@app.route('/')
def home():
    return render_template('index.html')


@app.route("/<string:page_name>")
def contact(page_name):
    return render_template(page_name)


@app.route('/appointment', methods=['POST', 'GET'])
def appointment():
    if request.method == 'POST':
        first_name = request.form.get('first-name')
        last_name = request.form.get('last-name')
        email = request.form.get('email')
        phone_number = request.form.get('number')
        date = request.form.get('date')
        service = request.form.get('service')


        client_data = {
            'First Name': first_name,
            'Last Name': last_name,
            'Email': email,
            'Phone Number': phone_number,
            'Date': date,
            'Service': service
        }
        try:
            with open('clients.csv', 'a', newline='') as csvfile:
                fieldnames = ['First Name', 'Last Name', 'Email', 'Phone Number', 'Date', 'Service']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                if csvfile.tell() == 0:
                    writer.writeheader()

                writer.writerow(client_data)

            sender = os.getenv('SENDER')
            receiver = {email}  
            subject = 'BOOKING APPOINTMENT'
            password = os.getenv('PASSWORD')
            capitalized_name = first_name.title()

            date_object = datetime.strptime(date, '%Y-%m-%d')
            formatted_date = date_object.strftime('%A %B %d, %Y')

            email = EmailMessage()
            email['From'] = 'Spencer Care Lounge'
            email['To'] = receiver
            email['Subject'] = subject
            

            email.set_content(f'Hello {capitalized_name}, \n\nYour appointment is set to be on {formatted_date} for {service}. We look forward to serving you.')

            
            with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
                smtp.ehlo()
                smtp.starttls()
                smtp.login(sender, password)
                smtp.send_message(email)
                print('Email sent successfully!')
                return redirect('/thanks.html')
            

        except Exception as e:
            print(f'Error: {e}')
            flash('An error occurred. Please try again.', 'error')
            return redirect('/appointment.html')

        


if __name__ == '__main__':
    app.run(debug=True)