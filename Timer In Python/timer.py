import time
from playsound import playsound


def alarm_clock():
    alarm = "alarm.wav"

    time_format = input(
        "Would you like hours (h), minutes (m), or seconds (s)? ")

    the_time = float(input("Please enter the time you would like: "))

    if time_format == "h":
        time.sleep(the_time * 3600)
        playsound(alarm)
    elif time_format == "m":
        time.sleep(the_time * 60)
        playsound(alarm)
    elif time_format == "s":
        time.sleep(the_time)
        playsound(alarm)
    else:
        print("Time format invalid.")

    print("Alarm went off.")


alarm_clock()

while True:
    again = input("Would you like to make another alarm (y/n)? ")
    if again == "y":
        alarm_clock()
    elif again == "n":
        print(f"You entered '{again}', Program quitting...")
        break
    else:
        print("You entered a not listed operation program quitting...")
        break
