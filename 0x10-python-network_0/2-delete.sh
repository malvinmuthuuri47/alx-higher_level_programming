#!/usr/bin/bash
# This script sends a DELETE request to the URL passed as the first argument and displays the body of the response
curl -sX "DELETE" "$1" 0.0.0.0:5000/route_3 ; echo ""
