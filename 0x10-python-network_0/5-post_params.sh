#!/bin/bash
# The script to get an URL, send a POST request and print the body of the response
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
