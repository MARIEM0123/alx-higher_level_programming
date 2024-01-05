#!/bin/bash
#The script to take an URL, send a request and display size of the request
curl -sI "$1" | grep -i Content-Length | cut -d " " -f 2
