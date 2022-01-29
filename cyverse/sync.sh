#!/bin/bash

# LOCAL_DIR="/path/to/experiment/dirs"
# REMOTE_DIR="i:/iplant/home/dgmendoz/DMC_phenotyping/DMC_photos/SRP/"

irsync -r -v ${LOCAL_DIR} ${REMOTE_DIR}
