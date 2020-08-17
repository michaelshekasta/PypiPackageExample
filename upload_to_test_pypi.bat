rmdir /s dist
rmdir /s build
rmdir /s pypi_package_example.egg-info
python setup.py sdist bdist_wheel
python -m twine upload --repository testpypi dist/*