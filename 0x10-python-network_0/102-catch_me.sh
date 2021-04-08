#!/bin/bash
# Makes loking for a respond with a message containing You got me!
curl 0.0.0.0:5000/catch_me -sL -X PUT -d "user_id=98" -H "Origin: HolbertonSchool"
