from flask import Flask, render_template, request
import smtplib

app = Flask(__name__)

email = "mypythontester24@gmail.com"
password = "pxiyewolnnloivze"

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/send', methods=["POST"])
def send():
    dict = request.values.to_dict()
    message = f"""
    Subject:{dict['subject']}\n\n
    From {dict['name']} - {dict['email']}\n
    {dict['message']}
    """
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email, to_addrs="isaac.trigoso@yahoo.com", msg=message)
    return render_template('index.html', success=True)

if __name__ == "__main__":
    app.run(debug=True)
