#!/bin/sh
# pulls mp areas

wget -r -I /v -w 2 --random-wait -U mozilla --accept-regex ".*\/v\/[a-z].*" https://www.mountainproject.com/destinations/