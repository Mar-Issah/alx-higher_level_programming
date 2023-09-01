#!/usr/bin/python3
""" script that fetches https://alx-intranet.hbtn.io/status """
import urllib.request as request


if __name__ == "__main__":
    with request.urlopen("https://intranet.hbtn.io/status") as response:
        body = response.read()
        print(f"Body response:\n\t- type: {type(body)}\n\t- content: {body}\n\t- utf8 content: {body.decode('utf-8')}")
