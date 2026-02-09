#!/bin/bash

# Replace this with your actual Render URL
URL="https://your-app-name.onrender.com"

echo "Starting keep-alive script for $URL"

while true
do
  # Perform a silent request to the URL
  curl -s $URL > /dev/null
  
  # Get the current timestamp for the log
  TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
  
  echo "[$TIMESTAMP] Pinged $URL to stay awake."
  
  # Wait for 5 minutes (300 seconds)
  sleep 300
done