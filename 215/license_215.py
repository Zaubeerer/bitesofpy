import re


def validate_license(key: str) -> bool:
    """Write a regex that matches a PyBites license key
       (e.g. PB-U8N435EH-PG65PW87-IXPWQG5T-898XSZI4)
    """
    if len(key) == len("PB-U8N435EH-PG65PW87-IXPWQG5T-898XSZI4"):
        return bool(re.match('PB-[A-Z0-9_]{8}-[A-Z0-9_]{8}-[A-Z0-9_]{8}-[A-Z0-9_]{8}', key))
    else:
        return False