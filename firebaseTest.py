import pyrebase

config = {
  "apiKey": "AIzaSyD10CLaTTI30Bb1dCbTAmnOmmro2r71Pig",
  "authDomain": "plantbuddy.firebaseapp.com",
  "databaseURL": "https://plantbuddy-7e5ce.firebaseio.com",
  "storageBucket": "PlantBuddy.appspot.com"
}

'''
	initialize app with config
'''
firebase = pyrebase.initialize_app(config)

'''
	authenticate a user
'''
auth = firebase.auth()
user = auth.sign_in_with_email_and_password("markdaleman@icloud.com", "Welkom#1")


db = firebase.database()

'''
	Create using push
'''
archer = {"name": "Sterling Archer", "agency": "Figgis Agency"}
db.child("agents").push(archer, user['idToken'])

pam = {"name": "Pam Poovey", "agency": "Figgis Agency"}
db.child("staff").push(pam, user['idToken'])


'''
	Create using set
'''

lana = {"name": "Lana Kane", "agency": "Figgis Agency"}
db.child("agents").child("Lana").set(lana, user['idToken'])

kreiger = {"name": "Algernop Kreiger", "agency": "Figgis Agency"}
db.child("staff").child("Krieger").set(kreiger, user['idToken'])

'''
	Get all users
'''
all_agents = db.child("agents").get(user['idToken'])
print("all_agents: ", all_agents)

'''
	Get specific value from object
'''
lana_data = db.child("agents").child("Lana").get(user['idToken']).val()
print ("lana_data: ", lana_data["agency"])

'''
	Update existing user
'''
db.child("agents").child("Lana").update({"name": "Lana Anthony Kane"}, user['idToken'])

'''
	Delete entire object
'''
db.child("staff").remove(user['idToken'])

'''
	Delete specific value from object
'''
db.child("agents").child("Lana").remove(user['idToken'])
