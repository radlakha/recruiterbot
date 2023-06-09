import os
from dotenv.main import load_dotenv 

import requests
# from flask_recaptcha import ReCaptcha
from flask import *
from flask_mail import Mail, Message
from flask_sqlalchemy import SQLAlchemy # A basic SQL databse

import uuid  # for public id
import jwt   # for JWT creation
from datetime import datetime, timedelta # for encoding time of creation

from bs4 import BeautifulSoup as bs # Editing HTML through python

def create_mail_body(token):
	basePath = os.path.dirname(os.path.abspath(__file__))+"/templates/"
	html = open(os.path.join(basePath, 'email_response_template.html'))
	emailTemplate = bs(html, 'html.parser')

	linkLocation = emailTemplate.find('a')
	linkLocation['href'] = "http://127.0.0.1:5000/user?token="+ str(token, 'utf-8')

	return str(emailTemplate)


load_dotenv()

app = Flask(__name__)

captchaSiteKey = os.environ['CAPTCHA_SITE_KEY']
captchaSecretKey = os.environ['CAPTCHA_SECRET_KEY']
app.config.update({'RECAPTCHA_ENABLED': True,
				   'RECAPTCHA_SITE_KEY':
				   captchaSiteKey,
				   'RECAPTCHA_SECRET_KEY':
				   captchaSecretKey})


# recaptcha = ReCaptcha(app=app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = os.environ['MAIL_USERNAME']
# Generated App Password for the email
app.config['MAIL_PASSWORD'] = os.environ['MAIL_PASSWORD']
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

hashingAlgorithm = os.environ['HASHING_ALGORITHM']

database = SQLAlchemy(app)
mailApp = Mail(app)


class User(database.Model):
	id = database.Column(database.Integer, primary_key=True)
	public_id = database.Column(database.String(50), unique=True)
	email = database.Column(database.String(70), unique=True)


@app.route("/")
def index():
	return render_template("home.html")


@app.route("/send_mail", methods=['post'])
def send_mail(**kwargs):
	if request.method == 'POST':
		googleResponse = requests.post('https://www.google.com/recaptcha/api/siteverify',
						  data={'secret':
								captchaSecretKey,
								'response':
								request.form['g-recaptcha-response']})

		googleResponse = json.loads(googleResponse.text)
		# print('JSON: ', googleResponse) #debug

		if googleResponse['success']:
			# print('SUCCESS')
			email = request.form['email'].strip()
			subject = 'Your door to the chatroom'
			admin = os.environ['MAIL_USERNAME']

			#Find user in database
			user = User.query\
				.filter_by(email=email)\
				.first()
			
			if not user:
				#Create user
				# database ORM object
				user = User(
					public_id=str(uuid.uuid4()),
					email=email,
				)
				database.session.add(user)
				database.session.commit()

			token = jwt.encode({
				'public_id': user.public_id,
				'exp': datetime.utcnow() + timedelta(minutes=30)
			}, app.config['SECRET_KEY'], hashingAlgorithm)

			mailBody = create_mail_body(token)
			mailMessage = Message(subject=subject, sender=admin,
							  recipients=email.split(), html=mailBody)
			mailApp.send(mailMessage)
			return render_template("submit.html")

		else:
			# Reroute to home page if captcha fails 
			return redirect('/')


#Just a dummy route for the chatroom, prints the email which was used to sign-in
@app.route('/user', methods=['GET'])
def get_all_users():
	args = request.args
	token = args.get('token')
	data = jwt.decode(token, app.config['SECRET_KEY'], hashingAlgorithm)

	users = User.query.all()
	output = []
	for user in users:
		if user.public_id == data['public_id']:
			output.append({
				'email': user.email
			})
	return jsonify({'users': output})


if __name__ == '__main__':
	app.run()
