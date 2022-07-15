#!/usr/bin/python3
"""Alta3 Research - Exploring Astronaut API with requests"""
# documentation for this API is at
# https://api.open-notify.org

import pprint
import requests

AOIF = "http://api.open-notify.org/astros.json"

def main():
    ## Send HTTPS GET to the API of Astronauts
    gotresp = requests.get(AOIF)

    ## Decode the response
    got_dj = gotresp.json()

    ## print the response
    ## using pretty print so we can read it
    pprint.pprint(got_dj)
if __name__ == "__main__":
    main()

