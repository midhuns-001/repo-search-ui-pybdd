# UI Testing with Selenium Python & Pytest BDD - Page Object Model

## Overview
This project provides an example for testing a UI with Selenium WebDriver, written in Python, using the Page Object Model design pattern and driven via BDD feature files through Pytest BDD. It can be used to kickstart testing of other UIs with minimal changes to the project.


## Web Application Under Test
The website that is being tested by this framework is “Repository Search”, that uses Repository APIs to make search when a given keyword is passed into the field

Following functionality has been tested, focusing on the following pages:
* [home/repository-list](http://localhost:3000/) page


### Tech stack
As this is a Python project, build and dependency management is handled by Pipenv, so there is a `Pipfile` (and associated `.lock` file) defining the versions of the dependencies:
* Python v3.8
* Selenium v4.1.5
* Pytest v7.1.2
* Pytest BDD v5.0.0
* Sstable v0.0.1
* Webdriver-Manager v3.5.4
* Pytest-html v3.1.1

Follow below steps to setup this project

* Install pipenv. pip install pipenv
* Install Pipfile and create environment. pipenv install Pipfile
* Activate environment. pipenv shell



### Supported Browsers
The `conftest.py` module uses the Webdriver-Manager dependency to manage the various browser drivers. The `browser` Pytest fixture returns the relevant WebDriver instance for the chosen browser, with support for:
* Chrome - the default option
* Firefox


### Running tests

Example: pytest -m repo_list_home_page --html=report.html


#### Test Reports


