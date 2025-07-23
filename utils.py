def add_url_scheme(url):
    if "https://" in url: return url
    else:
        if "http://" in url: return url.replace("http://", "https://")
        else: return "https://" + url

def get_mode(url):
    # returns variants based on which we will later crawl github
    # should return either 'user_profile', 'organization', 'repo' or unsupported 
    #
    # pogledaj kako se radi docstring
    # returns tuple
    url_keywords = [
            "/marketplace",
            "/actions",

        ]
    if any(url_keyword in url for url_keyword in url_keywords):
        return "unsupported"


