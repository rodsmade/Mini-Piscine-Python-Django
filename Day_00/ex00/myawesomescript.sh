#!/bin/sh

# Only letters, numbers, '-' and '_' allowed
curl -s $1 | grep href | cut --delimiter='"' --fields=2