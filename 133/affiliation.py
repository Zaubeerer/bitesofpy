def generate_affiliation_link(url, tag="pyb0f-20"):

    url_shortened = url.split("/")

    return f"http://www.amazon.com/{url_shortened[4]}/{url_shortened[5]}/?tag={tag}"
