@echo off
python setup.py sdist bdist bdist_wheel build
twine upload dist/*