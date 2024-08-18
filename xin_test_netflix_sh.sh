#!/bin/bash

hostname="netflix.com"
port=443

# Attempt to connect to the server
if nc -zv -w 10 $hostname $port 2>&1 | grep -q 'succeeded'; then
    echo "Successfully connected to $hostname on port $port"
else
    echo "Failed to connect to $hostname on port $port"
fi
