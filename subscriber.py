import paho.mqtt.client as mqtt
import ssl

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+ str(rc))
    client.subscribe("Pi/LED/#")
def on_message(client, userdata, msg):
    f = open("data.txt", "a")
    f.write(str(msg.payload)+"\n")
    f.seek(0)
    f.close()
    print(msg.topic+"  =>  "+str(msg.payload))
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("test.mosquitto.org", 1883, 60)
client.loop_forever()


