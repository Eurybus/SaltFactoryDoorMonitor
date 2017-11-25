import paho.mqtt.client as mqtt


class DoorClient(object):

    def __init__(self):
        print "Started MQTT client"
        client = mqtt.Client()
        client.on_connect = self.on_connect
        client.on_message = self.on_message
        client.username_pw_set('pwrspiob', password='mzH6meKV0hcg')
        client.connect("m23.cloudmqtt.com", 16730, 60)

    def on_connect(client, userdata, flags, rc):
        print("Connected with result code " + str(rc))

        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        client.subscribe("/open/door_01")
        client.subscribe("/close/door_01")

        client.subscribe("/close/door_02")

    def on_door_event(self, color, msg, time):
        pass

    # The callback for when a PUBLISH message is received from the server.
    @staticmethod
    def on_message(client, userdata, msg):
        print(msg.topic + " " + str(msg.payload))

        if msg.topic == '/open/door_01':
            pass # TODO