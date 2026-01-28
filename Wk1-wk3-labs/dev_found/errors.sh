#!/bin/bash
MAX_RETRIES=5
SLEEP_INTERVAL=3
RETRYABLE_ERROR=1

retries=0

while [ $retries -lt $MAX_RETRIES ]; do
    # Run an HTTP request 
    curl -I https://aws.amazon.com
    if [ $? -eq 0 ]; then
        # Successful command, exit the loop
        break
    else
        # Retryable error, increment retries and sleep before the next attempt
        retries=$((retries + 1))
        sleep $SLEEP_INTERVAL
    fi

done
if [ $retries -eq $MAX_RETRIES ]; then
    echo "Maximum retry attempts reached. Exiting script."
    exit 1
fi