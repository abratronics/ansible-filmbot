#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

# search for horror and sci-fi, sort prices from low to high
filmfreeway_url = "https://filmfreeway.com/festivals?utf8=%E2%9C%93&config%5B%5D=niches&config%5B%5D=entry_fees&config%5B%5D=years_running&config%5B%5D=runtime&config%5B%5D=region&config%5B%5D=entry_deadline&config%5B%5D=submit&has_query=&ga_search_category=Festival&q=&call_for_entries=1&ft_gold=0&ft_ff=0&ft_sc=0&ft_audio=0&ft_photo=0&ft_oe=0&fees=0%3B100&years=1%3B20&runtime=Any&niche%5B%5D=8&niche%5B%5D=14&inside_or_outside_country=0&countries=us&entry_deadline_when=0&entry_deadline=&event_date_when=0&event_date=&sort=price_low"

horror_response = requests.get(filmfreeway_url)
horror_soup = BeautifulSoup(horror_response.content, "html.parser")

# Extract and print festival names
horror_festival_names = horror_soup.find_all("div", class_="BrowseFestivalsCard-name")
print("HORROR AND SCI-FI FOCUS - Open or Upcoming Festivals with Submissions:")
for name in horror_festival_names:
    if "Film Festival" in name.get_text():
        print(name.get_text().strip())
