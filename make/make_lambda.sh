#!/bin/bash -e

mkdir -p lambda

cd lambda

mkdir -p lambda_function_package

cp -r ../../src/app.py ../../src/connections ../../src/utils lambda_function_package/

cd lambda_function_package/

zip -r ../lambda_function.zip .

cd ..

read -p "Digit Python Version. Exemple: python3.8 " version_python

mkdir -p python/lib/$version_python/site-packages

$version_python -m pip install -U \
  pip setuptools wheel testresources importlib_metadata --no-cache-dir && \
  $version_python -m pip install -r ../../requirements.txt \
  -t ./python/lib/$version_python/site-packages/ --no-cache-dir

zip -r layer_dependencies.zip python

rm -rf lambda_function_package
rm -rf python

echo "Packages 'lambda_function.zip' and 'layer_dependencies.zip' created in the directory 'lambda'."
