from datetime import datetime
import pytz

color = {
    'RED': '\033[1;91m',
    'UNDERLINE_PURPLE': '\033[4;34m',
    'GREEN': '\033[1;92m',
    'YELLOW': '\033[1;33m',
    'CYAN': '\033[0;36m',
    'PURPLE': '\033[0;34m',
    'MAGENTA': '\033[0;35m',
    'DEFAULT': '\033[0m',
    'TWITTER_BLUE': '\033[38;5;33m',
}
country_zones = ["Africa/Algiers", "Africa/Casablanca",
                 "Africa/Tunis", "Africa/Cairo", "Africa/Khartoum"]

country_time_zones = []

for country_time_zone in country_zones:
    country_time_zones.append(pytz.timezone(country_time_zone))

for i in range(len(country_time_zones)):
    country_time = datetime.now(country_time_zones[i])
    print(f"{color['DEFAULT']}The date in {color['RED']}'{country_zones[i]}': {color['GREEN']}{country_time.strftime('%d-%m-%y')} {color['DEFAULT']}and The Time: {color['PURPLE']}{country_time.strftime('%H:%M')}\n")
