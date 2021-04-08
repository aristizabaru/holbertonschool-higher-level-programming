#!/usr/bin/env bash
# Sends a POST request to the passed URL, and displays the body of the response
curl -s "$1" -X POST -d "email=hr@holbertonschool.com&subject=I%20will%20always%20be%20here%20for%20PLD"
