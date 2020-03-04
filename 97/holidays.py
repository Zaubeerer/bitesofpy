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
    soup = BeautifulSoup(content, "html.parser")

    table_text = soup.find_all("table")[0]

    name_pattern = 'title=\"\">[\s\S]*?<\/a>'
    date_pattern = 'datetime=\"[\s\S]*?\"'

    re_name_patterns = re.findall(name_pattern, content)
    names = [string[9:-4].strip() for string in re_name_patterns]

    re_date_patterns = re.findall(date_pattern, content)
    dates = [string[15:-4] for string in re_date_patterns]

    holiday_dict = defaultdict(list)

    for date, holiday_name in zip(dates, names):
        holiday_dict[date].append(holiday_name)

    return holiday_dict