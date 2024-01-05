#!/bin/bash
# THE script to send a DELETE request to the URL and display the body of the response
curl -s "$1" -X DELETE
