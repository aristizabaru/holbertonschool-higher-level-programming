#!/bin/bash
# Makes loking for a respond with a message containing You got me!
curl 0.0.0.0:5000/catch_me -sL -X PUT -d "user_id=98" -H "Origin: HolbertonSchool"


#!/bin/bash
# Makes a request to 0.0.0.0:5000/catch_me that gets the message "You got me!".
curl -sL -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me