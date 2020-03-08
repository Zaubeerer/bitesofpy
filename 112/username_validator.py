# nice snippet: https://gist.github.com/tonybruess/9405134
import re
from collections import namedtuple

social_platforms = """Twitter
  Min: 1
  Max: 15
  Can contain: a-z A-Z 0-9 _

Facebook
  Min: 5
  Max: 50
  Can contain: a-z A-Z 0-9 .

Reddit
  Min: 3
  Max: 20
  Can contain: a-z A-Z 0-9 _ -
"""

# note range is of type range and regex is a re.compile object
Validator = namedtuple('Validator', 'range regex')


def parse_social_platforms_string():
    """Convert the social_platforms string above into a dict where
       keys = social platformsname and values = validator namedtuples"""
    # pseudo code:
    platform_dict = {}

    for social_platform_string in re.split(r'\n\n', social_platforms):
        lines = re.split(r'\n', social_platform_string)
        # TODO: rewrite this using groups, something like:
        # m = re.match(r'((?P<description>\w+): (?P<value>\w+) \n)*', 'Jane Doe')

        platform_name = lines[0]
        range_min = int(lines[1][7:])
        range_max = int(lines[2][7:])
        allowed_characters = re.sub(' ', '', f'{lines[3][14:]}')
        regex = re.compile(fr"^[{allowed_characters}]+$")

        platform_dict[platform_name] = Validator(range(range_min, range_max), regex)

    return platform_dict



def validate_username(platform, username):
    """Receives platforms(Twitter, Facebook or Reddit) and username string,
       raise a ValueError if the wrong platform is passed in,
       return True/False if username is valid for entered platform"""
    all_validators = parse_social_platforms_string()


    try:
        regex = all_validators[platform].regex
        # pattern = fr"[{regex}]{{{len(username)}}}"
        if len(username) in all_validators[platform].range:
            return re.match(regex, username)
    except:
        raise ValueError("Wrong platform passed in")
