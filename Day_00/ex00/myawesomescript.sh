#!/bin/sh

# Only letters, numbers, '-' and '_' allowed
curl -s bit.ly/rodsmade | grep href | cut --delimiter='"' --fields=2