#!/bin/bash

MAX_LOG_SIZE=1000000
CURRENT_LOG_SIZE=$(wc -c < "script.log")

if [ "$CURRENT_LOG_SIZE" -gt "$MAX_LOG_SIZE" ]; then
    mv "script.log" "script.log.old"
    touch "script.log"
fi.
