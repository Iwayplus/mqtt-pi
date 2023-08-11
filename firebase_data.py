import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Initialize the Firebase app
cred = credentials.Certificate('uwb-loc-log-firebase-adminsdk-rx3ph-b53747ed9e.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://uwb-loc-log-default-rtdb.firebaseio.com/'
})

# Get a reference to the database root
root_ref = db.reference()

# Stream data to a specific location
data_ref = root_ref.child('your_data_location')


topic = 'dwm/node/0d13/uplink/location'
Message = {"position":{"x":18.734064,"y":61.619366,"z":0.35824484,"quality":93},"superFrameNumber":79}
# Stream individual data points
data_ref.push(Message)
