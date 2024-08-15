#!/bin/bash
# This is a simple example of how to use the boilerplate module using the command line.

uv pip install -e . >> /dev/null 2>&1 \
&& boilerplate -v 2 3 \
&& uv pip uninstall . >> /dev/null 2>&1
