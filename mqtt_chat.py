# MWE of an encrypted chat using MQTT
import paho.mqtt.client as paho
import os

def on_message(client, userdata, msg):
    print str(msg.payload)

def on_connect(client, userdata, rc):
    print "Entering.."
    mqttc.publish(topic, user+" has entered", 0)

def on_disconnect(client, userdata, rc):
    print "Leaving.."

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
cacert = BASE_DIR + "/keys/mosquitto.org.crt"
cert   = BASE_DIR + "/keys/client.crt" # The client certificates and keys are generated using openssl
key    = BASE_DIR + "/keys/client.key"
user  = raw_input('Enter your nick name\n')
topic = raw_input('Enter topic name\n')
mqttc = paho.Client()
mqttc.on_message    = on_message
mqttc.on_connect    = on_connect
mqttc.on_disconnect = on_disconnect
mqttc.tls_set(cacert, cert, key)
mqttc.connect("test.mosquitto.org", 8883)
#mqttc.connect("localhost", 8883)
mqttc.subscribe(topic)
mqttc.loop_start()

if __name__ == "__main__":
    try:
        while True:
            msg = raw_input()
            msg = "["+user+"] "+msg
            mqttc.publish(topic, msg, 0)
    except KeyboardInterrupt:
        mqttc.publish(topic, user+" has left", 0)
        mqttc.loop_stop()
        mqttc.disconnect()
