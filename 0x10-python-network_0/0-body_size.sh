#!/bin/bash
# displaying size of response body
body_size=$(curl -s "$1" | wc -c)
echo "$body_size"
