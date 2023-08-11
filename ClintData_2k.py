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

# Define the maximum number of samples to keep in the window
MAX_SAMPLES = 20

# Create a dictionary to hold data for each topic
topics_data = {}

# List of topics to subscribe to
topics = [
    "dwm/node/4aec/uplink/config",
    "dwm/node/4aec/uplink/location",
    "dwm/node/0d13/uplink/config",
    "dwm/node/0d13/uplink/location",
    "dwm/node/2016/uplink/config",
    "dwm/node/2016/uplink/location"
]

# Initialize data dictionary for each topic
for topic in topics:
    topics_data[topic] = []

# Callback function for successful connection
def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker")
    # Subscribe to topics
    for topic in topics:
        client.subscribe(topic)

# Callback function for incoming messages
def on_message(client, userdata, msg):
    data = msg.payload.decode()
    res = json.loads(data)
    topic = msg.topic

    # Append the new data to the topic's data list
    if len(topics_data[topic]) >= MAX_SAMPLES:
        topics_data[topic].pop(0)
    topics_data[topic].append(res)

    # Update data in Firebase for the specific topic
    data_ref = db.reference(topic)
    data_ref.set(topics_data[topic])

    print("Data received on topic:", topic)
    print("Message:", res)
    print("==========================")

# Create an MQTT client instance
client = mqtt.Client()

# Set the callback functions
client.on_connect = on_connect
client.on_message = on_message

# Connect to the MQTT broker
client.connect("10.194.101.194", 1883, 60)

# Start the MQTT client loop
client.loop_forever()
