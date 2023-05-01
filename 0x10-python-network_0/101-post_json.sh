#!/bin/bash
# This script sends a JSON POST request to a URL passed as the first argument and displays the body of the response
#!/bin/bash
curl -s -H  "Content-Type: application/json" "$1" -d "$(cat "$2")"
