#!/bin/bash
# y
curl -s -v "$1" --stderr - | grep Content-Length: | cut -d' '  -f 3
