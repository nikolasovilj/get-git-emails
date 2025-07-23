import requests
import sys
import os
import argparse
from utils import add_url_scheme


def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument(
            "url", help="url to github profile, organization or repository", type=str
    )
    parser.add_argument(
            "--include-forks",
            action="store_true",
            help="scrape emails from forked repos"
    )
    
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    args = parser.parse_args()
    
    url = args.url
    url = add_url_scheme(url)
    include_forks = args.include_forks
    
    print(f"url: {url}")
    print(f"Using forks: {include_forks}")


if __name__ == '__main__':
    main()
