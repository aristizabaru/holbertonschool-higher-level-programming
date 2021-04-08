#!/bin/bash
# Sends a GET request to the URL with headers, and displays the body of the response
curl -s "$1" -X GET -H "X-HolbertonSchool-User-Id: 98"
