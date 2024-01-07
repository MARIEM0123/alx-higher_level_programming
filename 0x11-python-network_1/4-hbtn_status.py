#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status.

Usage: ./4-hbtn_status.py <URL>
  - Handles HTTP errors.
"""
import requests

url = 'https://alx-intranet.hbtn.io/status'

response = requests.get(url)
content = response.text

print("Body response:")
print("\t- type:", type(content))
print("\t- content:", content)
