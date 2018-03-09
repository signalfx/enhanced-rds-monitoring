#!/bin/bash

# Copyright (C) 2018 SignalFx, Inc. All rights reserved.

# Removes the ZIP file and build dependencies

set -e

BASE_PATH="$(pwd)/$(dirname $0)"
NAME=enhanced_rds
BUILD_DIR=$BASE_PATH/build/
TARGET=$NAME.zip

echo "Removing $TARGET from $BASE_PATH ..."

# Remove ZIP file.
rm $TARGET

echo "Removing $BUILD_DIR from $BASE_PATH ..."

# Remove old dependencies.
rm -r $BUILD_DIR