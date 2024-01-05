#!/bin/bash 
# The script to send a request to an URL  and print  the status code.
curl -s -L -X HEAD -w "%{http_code}" "$1"
