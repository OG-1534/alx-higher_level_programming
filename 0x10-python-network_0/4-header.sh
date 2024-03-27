#!/bin/bash
# script takes in a URL, sends a GET request, displays the body of the response
curl -sH "X-School-User-Id: 98" "$1"
