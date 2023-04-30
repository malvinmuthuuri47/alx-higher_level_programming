#!/bin/bash
# This script sends a request to a URL passed as an argument, and diplays only the status code of the response.
curl -sI "$1" -o /dev/null -w "%{http_code}"
