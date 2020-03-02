import os
from collections import Counter
import urllib.request
import re

# prep
tempfile = os.path.join('/tmp', 'feed')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/feed',
    tempfile
)

with open(tempfile) as f:
    content = f.read().lower()


# start coding

def get_pybites_top_tags(n=10):
    """use Counter to get the top 10 PyBites tags from the feed
       data already loaded into the content variable"""

    xml_pattern = "<category>[\s\S]*?<\/category>"

    # TODO: there most be a more suitable re.method() than the following combination:
    re_xml = re.findall(xml_pattern, content)
    categories = [string[10:-11] for string in re_xml]

    top_tag_counter = Counter(categories)

    return top_tag_counter.most_common(n)