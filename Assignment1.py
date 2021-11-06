import time
import requests
from requests.structures import CaseInsensitiveDict
import pin_controller as pctrl

# The last three digits of my A#: A00230066 is 666; Replacing the 0 with the maximum digit af last three


def run_question_one():
    period = 1  # Seconds
    # Turn all LEDs ON for 1 second
    pctrl.all_on()
    time.sleep(period)
    # Turn all LEDs OFF for 1 second
    pctrl.all_off()
    time.sleep(period)
    # Turn LED a ON for 1 second
    pctrl.pin_on(22)
    time.sleep(period)
    # Turn LED a OFF for 1 second
    pctrl.pin_off(22)
    time.sleep(period)
    # Turn LED b ON for 1 second
    pctrl.pin_on(22)
    time.sleep(period)
    # Turn LED b OFF for 1 second
    pctrl.pin_off(22)
    time.sleep(period)
    # Turn LED c ON for 1 second
    pctrl.pin_on(22)
    time.sleep(period)
    # Turn LED c OFF for 1 second
    pctrl.pin_off(22)
    time.sleep(period)
    # Run the stobe_reg method
    pctrl.strobe_reg()
    # Turn all LEDs OFF when keyboard interrupt is received before proceeding
    pctrl.all_off()


def run_question_two():
    on_period = 3  # Seconds
    off_period = 2  # Seconds
    iterations = 3
    url = 'http://localhost:5000/pins/1'
    body_on_state = "{\"pin_num\": 22, \"color\": \"red\", \"state\": \"on\"}"
    body_off_state = "{\"pin_num\": 22, \"color\": \"red\", \"state\": \"off\"}"
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"

    for i in range(iterations):
        resp = requests.put(url, headers=headers, data=body_on_state)
        print(f"Turning ON for {on_period} seconds...")
        print(f"Status Code: {resp.status_code}")
        time.sleep(on_period)
        resp = requests.put(url, headers=headers, data=body_off_state)
        print(f"Turning OFF for {off_period} seconds...")
        print(f"Status Code: {resp.status_code}")
        time.sleep(off_period)


if __name__ == '__main__':
    run_question_one()
    run_question_two()
