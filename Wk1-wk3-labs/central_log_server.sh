#!/bin/bash

CENTRAL_LOG_SERVER='central-log-server.com'
LOG_FILE='script.log'

scp "$LOG_FILE" "#CENTRAL_LOG_SERVER:/path/to/central/logs/"
# SCP command to transfer the log file to the central log server
