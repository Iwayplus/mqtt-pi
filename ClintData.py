import paho.mqtt.client as mqtt
import json
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
# data_ref = root_ref.child('your_data_location')

# Define individual arrays for each topic
config_data_4aec = []
location_data_4aec = []

config_data_0d13 = []
location_data_0d13 = []

config_data_2016 = []
location_data_2016 = []


# Callback function for successful connection
def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker")
    # Subscribe to topics
    client.subscribe("dwm/node/4aec/uplink/config")
    client.subscribe("dwm/node/4aec/uplink/location")
    
    client.subscribe("dwm/node/0d13/uplink/config")
    client.subscribe("dwm/node/0d13/uplink/location")
    
    client.subscribe("dwm/node/2016/uplink/config")
    client.subscribe("dwm/node/2016/uplink/location")

# Callback function for incoming messages
def on_message(client, userdata, msg):
    data = msg.payload.decode()
    res = json.loads(data)
    attributes = dir(msg)
    # print(attributes)
    # Extract topic name from the received message
    topic = msg.topic
    # sample = sample+1
    if topic == "dwm/node/4aec/uplink/config":
        config_data_4aec.append(res)
   
    elif topic == "dwm/node/4aec/uplink/location":
        location_data_4aec.append(res)
        data_ref = root_ref.child(topic)
        data_ref.push(data)
        print("Data received on topic:", topic)
        print("Message:", res["position"])
   
    elif topic == "dwm/node/0d13/uplink/config":
        config_data_0d13.append(res)
  
    elif topic == "dwm/node/0d13/uplink/location":
        location_data_0d13.append(res)
        data_ref = root_ref.child(topic)
        data_ref.push(data)
        print("Data received on topic:", topic)
        print("Message:", res["position"])
  
    elif topic == "dwm/node/2016/uplink/config":
        config_data_2016.append(res)
  
    elif topic == "dwm/node/2016/uplink/location":
        location_data_2016.append(res)
        data_ref = root_ref.child(topic)
        data_ref.push(data)  # res["position"]
        print("Data received on topic:", topic)
        print("Message:", res["position"])

    
    
    
    print("==========================")
    # if sample == 1000:
    #     # Get a reference to the Firebase database
    #     ref = db.reference('https://console.firebase.google.com/u/1/project/uwb-loc-log/database/uwb-loc-log-default-rtdb/data/~2Fdwm')
    #     # Delete data at the specified reference
    #     ref.delete()
    #     print('Data deleted successfully.')
    #     sample = 0

    # data_ref = root_ref.child(topic)
    # data_ref.push(data)

# Create an MQTT client instance
client = mqtt.Client()

# Set the callback functions
client.on_connect = on_connect
client.on_message = on_message

# Connect to the MQTT broker
client.connect("10.194.101.194", 1883, 60)

# Start the MQTT client loop
client.loop_forever()



