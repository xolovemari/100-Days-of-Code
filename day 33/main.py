import requests
import smtplib
import time
from datetime import datetime

# config
MY_LAT = 51.507351
MY_LONG = -0.127758 
MY_EMAIL = "example@gmail.com"
MY_PASSWORD = "example"
TO_EMAIL = "example@myyahoo.com" 

# is ISS close?
def is_ISS_close():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # ISS must be = 5 or -5 close
    if abs(MY_LAT - iss_latitude) <= 5 and abs(MY_LONG - iss_longitude) <= 5:
        return True
    return False

# is night check
def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now < sunrise:
        return True
    return False

# email
def send_email():
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=TO_EMAIL,
            msg="Subject:Look up! 👆\n\nThe ISS is passing above you in the sky!"
        )

# must happen every 60 sec
while True:
    if is_ISS_close() and is_dark():
        send_email()
        print("E-mail enviado! Olhe para o céu.")
    else:
        print("A ISS não está visível no momento.")
    time.sleep(60)