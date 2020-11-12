import paho.mqtt.client as paho
import json
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-o', '--ON', metavar='N ...',  type=int, nargs='*', help='Turn ON')
parser.add_argument('-f', '--OFF', metavar='N ..', type=int, nargs='*', help='Turn OFF')
parser.add_argument('--rgb', metavar='N N N', type=int, nargs='*', help='RGB colors')
#parser.add_argument('--sum', dest='accumulate', default=max, help='sum the integers (default: find the max)')

args = parser.parse_args()

print(type(args.ON))

broker="test.mosquitto.org"
port=1883

def on_publish(client,userdata,result):
    print("data published \n")
    pass

client= paho.Client("control1")
client.on_publish = on_publish
#client1.will_set("sensors/pressure", payload="Offline", qos=1, retain=True)
client.connect(broker,port)
client.publish("Pi/LED/Ledon",json.dumps(args.ON))
client.publish("Pi/LED/Ledoff",json.dumps(args.OFF))
client.publish("Pi/LED/RGB", json.dumps(args.rgb))
