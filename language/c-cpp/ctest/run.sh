#!/usr/bin/env bash
set -e
cmake -S. -B build;
cd build
make
./test_sqrt