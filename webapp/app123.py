from time import localtime, strftime
from flask import Flask, render_template, url_for
from firebase_admin import credentials
from firebase_admin import db
import firebase_admin
from pyfcm import FCMNotification

push_service = FCMNotification(api_key="AAAA6oFTOZk:APA91bGV8mG3Qm5sVNHc93ek8veiUEU80GcgzXEPYKbH1u0rOIvGAguj5yEDJaaPhKRMmH92bAyssEeE42hxLNrPhopM4rfLd-XRR6jDdSuUmKL1o3uoeuUCKGEzV5VzenOmNLlo3syo")

mToken = ""
n = 0


cred = credentials.Certificate('./FCM_key.json')
firebase_admin.initialize_app(cred,{
	'databaseURL' : 'https://fcmtest-2ed81.firebaseio.com/'
})

def sendMessage():
	global n
	n += 1
	registration_id = mToken

	data_message = {
		"body" : str(n) + "test"
	}

	message_title = "Push test"
	message_body = "Hi chiho"
	result = push_service.notify_single_device(registration_id = registration_id, message_title = message_title, message_body = message_body)
	print(result)


id = ""

tem = 99
gas = 300



app = Flask(__name__)

@app.route('/')
def index():

	return render_template('index1.html', temper=tem, gas=gas)

@app.route('/push')
def push():
	ref = 'users/'	
	new_ref = ref+id
	dir = db.reference(new_ref)
	
	temp = dir.get()
	for key in temp.keys():
		if(key == 'token'):
			mToken = temp[key]
			print(mToken)

	return render_template('index1.html', temper=tem, gas=gas)

@app.route('/id/<_id>')
def hello(_id):
	global id
	id = _id
	print(id)
	return render_template('index1.html',temper = tem, gas = id)



if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')