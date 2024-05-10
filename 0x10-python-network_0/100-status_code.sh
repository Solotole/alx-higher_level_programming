#!/bin/bash
# only displaying status code of a HTTP ressponse
curl -s -L -X HEAD -w "%{http_code}" "$1"
