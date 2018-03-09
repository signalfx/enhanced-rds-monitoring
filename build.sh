#!/bin/bash

# Copyright (C) 2017 SignalFx, Inc. All rights reserved.

# Builds the deployable ZIP file for the AWS Lambda function, with all of its
# dependencies.

set -e

BASE_PATH="$(pwd)/$(dirname $0)"
NAME=enhanced_rds
BUILD_DIR=$BASE_PATH/build/
TARGET=$NAME.zip

function cleanup() {
  rm -f $BUILD_DIR/setup.cfg
  cd $BASE_PATH
}

trap cleanup EXIT

echo "Building $TARGET from $BASE_PATH ..."

# Create build directory if it doesn't exist and go into it.
mkdir -p $BUILD_DIR
cd $BUILD_DIR

# Create a temporary setup.cfg file for DistUtils so it can install our
# dependencies into the given target correctly (required because of how
# HomeBrew's Python works).
cat > setup.cfg << EOF
[install]
prefix=
EOF

# Install dependencies
pip install -r ../requirements.txt --upgrade -t .

# Package everything up (all dependencies and lambda function code) into the
# same ZIP archive.
zip ../$TARGET -r *
cd ../$NAME
zip -u ../$TARGET *.py
