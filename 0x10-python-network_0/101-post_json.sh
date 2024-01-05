#!/bin/bash
# The script to send a JSON POST request to the URL and print the body of the response.
curl -s "$1" -d "@$2" -X POST -H "Content-Type: application/json"
