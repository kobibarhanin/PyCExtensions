#! /bin/bash

echo " => Building..."
python3 setup.py build

echo " => Copying artifacts..."
# may very in different os's and python versions
cp build/lib.macosx-10.9-x86_64-3.8/cModule.cpython-38-darwin.so .

echo " => Testing..."
python3 test.py

echo " => Cleaning..."
rm cModule.cpython-38-darwin.so
rm -rf build
