import time
import requests
from requests.structures import CaseInsensitiveDict
import pin_controller as pctrl

# The last three digits of my A#: A00230066 is 666; Replacing the 0 with the maximum digit af last three


def run_question_one():
    # Turn all LEDs ON for 1 second
    pctrl.all_on()
    time.sleep(1)
    # Turn all LEDs OFF for 1 second
    pctrl.all_off()
    time.sleep(1)
    # Turn LED a ON for 1 second
    pctrl.pin_on(22)
    time.sleep(1)
    # Turn LED a OFF for 1 second
    pctrl.pin_off(22)
    time.sleep(1)
    # Turn LED b ON for 1 second
    pctrl.pin_on(22)
    time.sleep(1)
    # Turn LED b OFF for 1 second
    pctrl.pin_off(22)
    time.sleep(1)
    # Turn LED c ON for 1 second
    pctrl.pin_on(22)
    time.sleep(1)
    # Turn LED c OFF for 1 second
    pctrl.pin_off(22)
    time.sleep(1)
    # Run the stobe_reg method
    pctrl.strobe_reg()
    # Turn all LEDs OFF when keyboard interrupt is received before proceeding
    pctrl.all_off()


def run_question_two():
    url = 'http://localhost:5000/pins/1'
    body_on_state = "{\"pin_num\": 22, \"color\": \"red\", \"state\": \"on\"}"
    body_off_state = "{\"pin_num\": 22, \"color\": \"red\", \"state\": \"off\"}"
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"

    for i in range(4):
        resp = requests.put(url, headers=headers, data=body_on_state)
        print("Turning ON for 3 seconds...")
        print(f"Status Code: {resp.status_code}")
        time.sleep(3)
        resp = requests.put(url, headers=headers, data=body_off_state)
        print("Turning OFF for 1 seconds...")
        print(f"Status Code: {resp.status_code}")
        time.sleep(1)


if __name__ == '__main__':
    run_question_one()
    run_question_two()
