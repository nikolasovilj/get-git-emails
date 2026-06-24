#!/usr/bin/env python3
import os, sys
import requests as r
from utils import get_next_link
import logging


logging.basicConfig(level=logging.INFO, format="{message}", style="{")

api_key = os.getenv("gh_api_key")
if not api_key:
    logging.info("make sure you set gh_api_key env variable!")
    sys.exit(1)

username = input("Enter GitHub username: ")

headers = {'Authorization': f'token {api_key}'}
url = f"https://api.github.com/users/{username}/repos?per_page=10&page=1"

repos = []

while True:
    res = r.get(url, headers=headers)
    for repo in res.json():
        logging.info(repo['name'])
        repos.append(repo['name'])
    logging.info(res.headers['Link'])
    try:
        url = get_next_link(res.headers['Link'])
    except Exception as e:
        logging.error("End of paginated repository discovery!")
        logging.error(e)
        break

logging.info(f"found {len(repos)} repos!")
logging.info(repos)

emails = set()
for repo in repos:
    url = f"https://api.github.com/repos/{username}/{repo}/commits"
    logging.info(f"getting: {url}")
    res = r.get(url, headers=headers)
    #logging.info(res.json())
    #logging.info(type(res.json()))
    for commit in res.json():
        try:
            #logging.info(commit['commit']['message'])
            #logging.info(commit['commit']['author']['email'])
            emails.add(commit['commit']['author']['email'])
            #logging.info(commit['commit']['committer']['email'])
            emails.add(commit['commit']['committer']['email'])
        except:
            pass

logging.info("\nemails found:")
for email in emails:
    if email: print(email)
