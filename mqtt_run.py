import paho.mqtt.client as mqtt
import json
# Callback function for successful connection
def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker")
    # Subscribe to a topic
    # client.subscribe("dwm/node/4aec/uplink/config")
    client.subscribe("dwm/node/4aec/uplink/location")
    
    # # client.subscribe("dwm/node/0d13/uplink/config")
    client.subscribe("dwm/node/490e/uplink/location")
    
    # # client.subscribe("dwm/node/2016/uplink/config")
    # client.subscribe("dwm/node/2016/uplink/location")

# Callback function for incoming messages
def on_message(client, userdata, msg):
    # print("Received message:", msg.payload.decode())
    data  = msg.payload.decode()
    res = json.loads(data)
    # pos_x = res["position"]['x']
    # pos_y = res["position"]['y']
    # quality = res["position"]["quality"]
    print(data)
    # print(pos_x, pos_y, quality)
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
