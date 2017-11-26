import sys
import os

import paho.mqtt.client as mqtt


def on_publish(client, userdata, mid):
    os.system('clear')
    print("{} published {} to {}".format(client, userdata, mid))

def main():
    client = mqtt.Client()
    client.on_publish = on_publish
    client.username_pw_set('pwrspiob', password='mzH6meKV0hcg')
    client.connect("m23.cloudmqtt.com", 16730, 60)

    while True:
        try:
            print(
                """
                FlowPro onStage:
                1. Door_01 OK
                2. Door_02 Unauthorized
                3. Door_02 OK
                4. Door_02 Unauthorized
                5. Elevator request
                0. Exit
                """
            )

            user_input = input("Select action: ")
            if user_input == 1:
                client.publish('/open/door_01', '{"door_01": True}')
            elif user_input == 2:
                client.publish('/close/door_01', '{"door_01": False}')
            elif user_input == 3:
                client.publish('/open/door_02', '{"door_02": True}')
            elif user_input == 4:
                client.publish('/close/door_02', '{"door_02": False}')
            elif user_input == 5:
                client.publish('/elevator', '{"elevator": True}')
            elif user_input == 0:
                raise SystemExit
            else:
                pass

        except (KeyboardInterrupt, SystemExit):
            print('FlowPro PlanB shutting down..')
            sys.exit(0)


if __name__ == "__main__":
    # execute only if run as a script
    main()
