#!/bin/bash
# displaying size of response body after sending url request
curl -sI "$1" | grep -i Content-Length | cut -d " " -f 2
