def get_next_link(link_header):
    links = link_header.split(", ")
    
    for link in links:
        if 'rel="next"' in link:
            next_link = link[link.find("<") + 1:link.find(">")]
            return next_link
    raise Exception
