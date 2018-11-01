#!/bin/sh

find . -name "*.pyc" -exec rm -Rf '{}' ';'

find . -name "__pycache__" -exec rm -Rf '{}' ';' 
