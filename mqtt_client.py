import paho.mqtt.client as mqtt
import threading
import json

latest_data = {}

def on_message(client, userdata, msg):
    global latest_data

    try:
        payload = msg.payload.decode()
        values = payload.split(',')

        latest_data = {
            "mA": float(values[0]),
            "mB": float(values[1]),
            "mC": float(values[2]),
            "dA": float(values[3]),
            "dB": float(values[4]),
            "dC": float(values[5]),
            "temp": float(values[6]),
            "hum": float(values[7]),
            "vA": int(values[8]),
            "vB": int(values[9]),
            "vC": int(values[10]),
            "pump": int(values[11])
        }
    except:
        pass

def start_mqtt():
    client = mqtt.Client()
    client.connect("broker.hivemq.com",1883)
    client.subscribe("farm/data")
    client.on_message = on_message
    client.loop_forever()

def run_mqtt():
    thread = threading.Thread(target=start_mqtt)
    thread.daemon = True
    thread.start()
