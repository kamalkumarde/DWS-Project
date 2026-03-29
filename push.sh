#!/bin/bash

# Check if a message was provided
if [ -z "$1" ]; then
    echo "❌ Error: Please provide a commit message."
    echo "Usage: ./push.sh 'your message here'"
    exit 1
fi

# Assign first argument to a variable
MESSAGE=$1

echo "🚀 Preparing to push to main..."

# Standard git flow
git add .
git commit -m "$MESSAGE"
git push -u origin main

echo "✅ Successfully pushed: $MESSAGE"