import requests
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import timezone

def reversephone(phonenumber):
    try:
        finalinfo = []

        r = requests.get(f"https://validnumber.com/phone-number/{phonenumber}/")

        for x in r.text.split("\n"):
            if '<div id="cnam">' in x:
                name = x.split('<div id="cnam">', 1)[-1].split(phonenumber[2], 1)[0].rstrip().lstrip()
                finalinfo.append(f"Name: {name}")

        url = f"https://api.telnyx.com/v1/phone_number/1{phonenumber}"
        r = requests.get(url)
        data = r.json()
        carrier = data['carrier']['name']
        linetype = data['carrier']['type']

        num = phonenumbers.parse(phonenumber, "US")
        isvalid = phonenumbers.is_valid_number(num)
        if isvalid == False:
            finalinfo.append("Invalid Phone Number")
            return finalinfo
        region = geocoder.description_for_number(num, "us")
        timez = timezone.time_zones_for_number(num)
        for line in timez:
            time = line
        
        finalinfo.append(f"Timezone: {time}")
        finalinfo.append(f"Region: {region}")
        finalinfo.append(f"Carrier: {carrier}")
        finalinfo.append(f"Type: {linetype}")


        return finalinfo
    except Exception as e:
        finalinfo.append(f"Error {e}")
        return finalinfo
