#!/bin/bash
# Sends a request to a URL passed as an argument, displays only the status code, no pipe/redirection
curl -s -o /dev/null -w "%{http_code}" "$1"
