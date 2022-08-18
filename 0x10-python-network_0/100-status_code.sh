#!/bin/bash
# yy
curl -so /dev/null --write-out "%{http_code}" "$1"
