#!/bin/bash

set -e

version_python="python$(python3 --version | awk '{print $2}' | cut -d. -f1,2)"

mkdir -p lambda

cd lambda

mkdir -p lambda_function_package

cp -r ../../src/lambda_function.py ../../src/connections ../../src/utils lambda_function_package/

find lambda_function_package/ -name "__pycache__" -type d -exec rm -rf {} +
rm -rf lambda_function_package/.venv
rm -f lambda_function_package/.env

cd lambda_function_package/

zip -r ../lambda_${version_python}_function.zip .

cd ..

mkdir -p python/lib/$version_python/site-packages

python3 -m pip install -U pip --no-cache-dir && \
  python3 -m pip install -r ../../requirements.txt \
  -t ./python/lib/$version_python/site-packages/ --no-cache-dir

zip -r layer_${version_python}_dependencies.zip python

rm -rf lambda_function_package
rm -rf python

echo "Packages 'lambda_function.zip' and 'layer_dependencies.zip' created in the directory 'lambda'."
