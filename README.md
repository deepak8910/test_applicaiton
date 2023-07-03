# Insurance Application

This is an insurance application built with FastAPI and pytest.
Make sure your system has python3 installed and pip installed, if it is not installed follow steps mentioned in this url to install it.
to download and install python:
https://www.python.org/downloads/

to install pip
https://packaging.python.org/en/latest/tutorials/installing-packages/

## Installation
To install the required packages, use the following command example:
pip install pytest

install all below packages in same way:
selenium, faker, fastapi, pydantic, typing, junit2html

# to start application run below command
python main.py

# to run test cases 
pytest test_api.py -sv --junitxml=results.xml --log-level=INFO --log-file=log_file.txt

# to convert xml result to html 
junit2html results.xml testrun.html

# There is one more file added test_policy_app_using_selenium.py in this project to test applicaiton using selenium web driver.
# however demo application is not ready to run this file, hence for now it cannot be run now.


