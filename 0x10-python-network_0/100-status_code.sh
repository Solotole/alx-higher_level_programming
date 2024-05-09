#!/bin/bash
# only displaying status code of a HTTP ressponse
curl -o /dev/null -w '%{http_code}' -sLI "$1"
