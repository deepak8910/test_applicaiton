# Insurance Application

This is an insurance application built with FastAPI and pytest.
Make sure your system has python3 installed and pip installed, if it is not installed follow steps mentioned in this url to install it.
to download and install python:
https://www.python.org/downloads/

# To install pip
https://packaging.python.org/en/latest/tutorials/installing-packages/

# Installation
To install the required packages, use the following command example:
pip install pytest

# Install all below packages in same way:
selenium, faker, fastapi, pydantic, typing, junit2html

# To create test data, this will create test_data.json
python create_policy_test_data.py

# To start application run below command, keep this tab open in the terminal
python main.py

# To run test cases, open new terminal and run below command
pytest test_api.py -sv --junitxml=results.xml --log-level=INFO --log-file=log_file.txt --html=reports/reports.html

# to see the html report
open reports/reports.html file in web browse to see the test report.

#part 2 
main2.py and test_api2.py files will be a short version shows if I want to send data to application via post method, how that can be done.
first start application by running "python main2.py" and then start test case in new terminal by running "pytest test_api2.py"

There is one more file added test_policy_app_using_selenium.py in this project to test applicaiton using selenium web driver.
However demo application is not ready to run this file, hence for now it cannot be run now.


