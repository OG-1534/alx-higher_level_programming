#!/bin/bash
# Bash script that gets the content-length of a giving URL in bytes
curl -sI "$1" | awk '/Content-Length/{print $2}'
