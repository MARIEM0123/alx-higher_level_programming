#!/bin/bash
# The script to take in a URL and display HTTP methods accepted
curl -s -I -X OPTIONS "$1" | grep "Allow:" | cut -f2- -d" "
