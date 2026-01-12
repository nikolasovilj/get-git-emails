#!/usr/bin/env python3
import os, sys
import requests as r

def get_next_link(link_header):
    # Split the Link header into individual link components
    links = link_header.split(", ")
    
    # Loop through the parts and find the "next" link
    for link in links:
        # Check if the 'rel="next"' is present
        if 'rel="next"' in link:
            # Extract the URL from the angle brackets
            next_link = link[link.find("<") + 1:link.find(">")]
            return next_link
    # Return None if no "next" link is found (i.e., end of pagination)
    raise Exception

api_key = os.getenv("gh_api_key")
if not api_key:
    print("make sure you set gh_api_key env variable!")
    sys.exit(1)

headers = {'Authorization': f'token {api_key}'}
username = input("Enter your username: ")
url = f"https://api.github.com/users/{username}/repos?per_page=10&page=1"
repos = []
while True:
    res = r.get(url, headers=headers)
    #print(res.status_code)
    for repo in res.json():
        print(repo['name'])
        repos.append(repo['name'])
    print(res.headers['Link'])
    try:
        url = get_next_link(res.headers['Link'])
    except Exception as e:
        print("End of paginated repository discovery!")
        print(e)
        break

print(f"found {len(repos)} repos!")
print(repos)

emails = set()
for repo in repos:
    url = f"https://api.github.com/repos/{username}/{repo}/commits"
    print(f"getting: {url}")
    res = r.get(url, headers=headers)
    #print(res.json())
    #print(type(res.json()))
    for commit in res.json():
        try:
            print(commit['commit']['message'])
            print(commit['commit']['author']['email'])
            emails.add(commit['commit']['author']['email'])
            print(commit['commit']['committer']['email'])
            emails.add(commit['commit']['committer']['email'])
        except:
            pass

print("emails found:")
for email in emails:
    print(email)
