# UI Testing with Selenium Python & Pytest BDD - Page Object Model

## Overview
This project provides an example for testing a UI with Selenium WebDriver, written in Python, using the Page Object Model design pattern and driven via BDD feature files through Pytest BDD. It can be used to kickstart testing of other UIs with minimal changes to the project.


## Web Application Under Test
The website that is being tested by this framework is “Repository Search”, that uses Repository APIs to make search when a given keyword is passed into the field

Following functionality has been tested, focusing on the following pages:
* [home/repository-list](http://localhost:3000/) page

## Test Framework
As stated above, this project contains a Selenium Python test framework, implements the Page Object Model design pattern and utilises Pytest BDD. As such, it follows test automation best practices. The Page Object Model means that each individual webpage has its own class, each containing the methods specific to controls on that page. Thus, each page is independent and separate from the tests, meaning any changes to the page are isolated to only the corresponding page class. This makes for code that is cleaner, easier to read and maintain, and contains less duplication. The use of Gherkin-style BDD means the tests themselves are also clean and clear, written in plain English, so they can be understood by anyone working with the project, including non-technical roles. Although this project is just an example of how to set up Selenium for UI testing in Python, in a real-life project the use of BDD is essential for collaboration between QAs, developers, and business roles (e.g. Product Owners, Business Analysts etc). Quality is everyone’s responsibility, which means the tests themselves need to be easily understood by all stakeholders.

### Tech stack
As this is a Python project, build and dependency management is handled by Pipenv, so there is a `Pipfile` (and associated `.lock` file) defining the versions of the dependencies:
* Python v3.8
* Selenium v4.1.5
* Pytest v7.1.2
* Pytest BDD v5.0.0
* Sstable v0.0.1
* Webdriver-Manager v3.5.4
* Pytest-html v3.1.1

### Project Structure
The project uses a standard structure and naming convention (hopefully):
* `features`  - this folder contains the Gherkin `.feature` files, one per website page. By separating out the tests for each page into separate feature files we continue the Page Object Model theme of page independence and make it easier to extend the framework in the future. Each feature file is named after the page it tests, e.g. `checkboxes_page.feature` contains the tests for the Checkboxes page.
* `pages` - the Page Object Model implementation of the individual website pages, one class file per page. Each class is named after the corresponding page e.g. `HomePage`, `DropdownPage` etc. Note, the filenames match the page names and do not match the class names exactly. For example, the `HomePage` class in the `home.py` file. There is also a `BasePage` which the other page classes implement/extend through inheritence.
* `step_defs` - a collection of files containing the implementation of the steps from the BDD feature files. As above, there is one steps file per page and each is named after the page under test, e.g. `test_dynamic_controls_page_steps.py`. The filename starts with `test_` as the project uses Pytest and this prefix is required in order for Pytest to recognise this file as a test file (with Pytest/Pytest BDD it is the steps files rather than the features that are executed as each steps file is bound to a feature file via the `scenarios` keyword - see [Running tests](#running-tests)).
NB Unlike the Java equivalent, there is no Common Steps files containing step definitions that are used by more than one feature file. This means there is some duplication of code across individual steps files at this stage, in particular for verifying the page title as I have declared the related variable and method as abstract in the base page class, meaning each page must define these. This is required as the HTML tag for the page title varies from page to page. Deduplicating these steps is something I have yet to work out how to properly resolve in Python.
* `config.json` - a JSON object used to define certain configuration options such as the browser, whether to run headless and the implicit wait timeout.
* `conftest.py` - this is _roughly_ equivalent to the `CommonSteps.java` class from the Selenium Java version of this project. This file contains methods to set up the browser (having read in the required parameters from the `config.json` file) and make that available to the page methods. It also sets up a few methods required to fully utilise data tables in feature files. Finally, steps that are common across multiple feature files (with the exception of the page title steps noted above) are contained within this file.

### Page Object Model Classes
As noted above, the `pages` folder contains the relevant Page Object Model classes for each tested page. Each page class, including the abstract `BasePage` class, follows the same pattern:
* selector/locator tuples declared as pairs, the first element being the locator method (`By.ID`, `By.XPATH` etc) and the second element being the locator itself (i.e. the ID, xpath etc).
* interaction methods e.g. to click on an element, get an element’s text etc. These methods use the above locator tuples, passing them to `find_element` or `find_elements` calls
  
This way we encapsulate the web elements themselves, only allowing the interactions that have been implemented via our methods, ensuring the tests (in effect, the user) can only interact with the web page in known ways.

The `BasePage` class defines constants for the URL for each page, ensuring they are available to methods within each individual page class. Also declared in the base class are a some common locators for elements used on multiple pages to avoid the need to declare the locator in each page class (following the DRY principle). Interaction methods for the page header and footer are declared in the `BasePage` class too, again to reduce code duplication. In order to get round the fact that the title element on the tested pages doesn't use a consistent HTML tag or class, an abstract `get_page_title_text` method is declared in the `BasePage` class ensuring that each individual page class implements a method to get the text of the page title, using a `PAGE_TITLE` locator specific to whatever to that page’s HTML uses for the title.

Note there are no assertions in the page classes as assertions are a test action rather than a page action. Page interaction methods will return the result of that interaction, such as the attribute or text value, to the calling method in the test steps classes, so that it can be asserted as correct there. In other words, we maintain independence between the tests and the pages.

### Supported Browsers
The `conftest.py` module uses the Webdriver-Manager dependency to manage the various browser drivers. The `browser` Pytest fixture returns the relevant WebDriver instance for the chosen browser, with support for:
* Chrome - the default option
* Firefox


### Running tests
The tests are easy to run as the project uses Pytest, so running the tests is as simple as running Pytest. As Pipenv is being used for dependency management this means running `pipenv run pytest` within the directory in which the repo has been cloned. The tests for an individual page can be run by passing the associated steps file as a parameter to the command, e.g. to run just the Checkboxes page tests `pipenv run pytest .\step_defs\test_checkboxes_page_steps.py`. Note that it is the steps file, rather than the feature file, which is specified. The steps file is bound to the corresponding feature via the `scenarios` keyword in the steps file, with the feature file path passed in as a parameter. The `browser` property can also be specified on the command line, e.g. `pipenv run pytest --browser Firefox` will run the test suite in Firefox.

NB Each test opens up in a separate browser instance (which is closed at the end of the test) so is not the fastest way to run a test suite, but it is the right way as we should ensure that tests are wholly independent of one another, do not share state and can run in any order. There are no `BeforeAll` and `AfterAll` hooks (that I am aware of), so we can’t open a single browser at the start of the test suite, navigate to the relevant page in the setup for each individual test scenario and close the browser at the end of the test suite. Having a separate browser per test also allows for test parallelisation which wouldn't otherwise be possible.

#### Test Reports
A report is generated for each test run as part of the GitHub Actions workflow (in the `Run tests` step). This is a simple report showing a list of the steps classes (each linked to a feature file) that have been executed and the overall result. In the event of a failing scenario, the details of the failure (actual versus expected result) are shown to allow easy debugging.

