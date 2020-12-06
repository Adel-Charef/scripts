from phonenumbers import geocoder
from phonenumbers import carrier
import phonenumbers

phone = "+YOURNUMBER"
ch_number = phonenumbers.parse(phone, "CH")
print(geocoder.description_for_number(ch_number, "en"))

service_number = phonenumbers.parse(phone, "RO")
print(carrier.name_for_number(service_number, "en"))
