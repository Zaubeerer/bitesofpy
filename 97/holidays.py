from collections import defaultdict
import os
from urllib.request import urlretrieve

from bs4 import BeautifulSoup

import re

from datetime import datetime

# prep data
tmp = os.getenv("TMP", "/tmp")
page = 'us_holidays.html'
holidays_page = os.path.join(tmp, page)
urlretrieve(
    f'https://bites-data.s3.us-east-2.amazonaws.com/{page}',
    holidays_page
)

with open(holidays_page) as f:
    content = f.read()

holidays = defaultdict(list)


def get_us_bank_holidays(content=content):
    """Receive scraped html output, make a BS object, parse the bank
       holiday table (css class = list-table), and return a dict of
       keys -> months and values -> list of bank holidays"""

    holiday_dict = defaultdict(list)

    soup = BeautifulSoup(content, "html.parser")
    table = soup.find("table", class_ = "list-table")

    rows = table.findAll('tr')
    for tr in rows[1:]:
        cols = tr.findAll('td')

        month = cols[1].findAll(text=True)[1][5:7]        
        name = cols[3].findAll(text=True)[1].strip()

        holiday_dict[month].append(name)

    return holiday_dict