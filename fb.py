import requests
from bs4 import BeautifulSoup

url = "https://mbasic.facebook.com/profile/timeline/stream/?cursor=AQHR2JoutnrudIw1oDfWsBW6XJpmDs4nD-MSWxw1QYMztfafPf8xKJT-ljxoqoMzYnBuIT37cKD73k4sIsTw7Vbnf-Pjw0V9POVXPqv1rv1ryelYGJD0Gq3LhrzpLtqWHJBE&start_time=-9223372036854775808&profile_id=100011668932981&replace_id=u_0_2&refid=17"
r = requests.get(url)

soup = BeautifulSoup(r.text, features='html.parser')

print(soup.title)
