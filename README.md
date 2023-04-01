## ------Note-------------
Test plan: Please refer the file "Test plan for automation the Regression tests on Upload features.docx".

Auto plan: Please refer the file "Automation plan for Upload Feature.xlsx". It also contains the road map for auto and test fw.
## ------------------------


## Overview
This proj provides an example for testing "Upload feature" with Selenium WebDriver, written in Python, using the POM design pattern and driven via BDD feature files through Pycharm. It can be used to kickstart testing of other UIs with minimal changes to the project. As I don't have the requirements of this demo page so I only write 1 sample scenario with my assumptions and show the test fw that is using, some abstracts items are the placeholders for later extensions

Notice that this is not a complete implementation of a Selenium test suite for the target UI. It is an example of how to structure a Selenium test suite in Python but only a subset of the possible tests have been added.

## Why Selenium is used?
Selenium is an open-source framework for testing web applications that is probably de facto the framework most people think of when it comes to UI testing. It supports a multitude of browsers (Chrome, Firefox, Safari, IE/Edge) as well as all major languages (there are bindings for Java, Python, JavaScript, C# and Ruby) making it suitable for almost any UI testing project. It is also highly portable so works across Windows, macOS and Linux/Unix and of course being open-source is freeware. There is an extensive and active Selenium community offering support for users and helping to extend and develop Selenium, which is always a bonus.

## Test Framework
As stated above, this project contains a Selenium Python test framework, implements the Page Object Model design pattern and utilises Pycharm BDD. As such, it follows test automation best practices. The POM means that each individual webpage has its own class, each containing the methods specific to controls on that page. Thus, each page is independent and separate from the tests, meaning any changes to the page are isolated to only the corresponding page class. This makes for code that is cleaner, easier to read and maintain, and contains less duplication. The use of Gherkin-style BDD means the tests themselves are also clean and clear, written in plain English, so they can be understood by anyone working with the project, including non-technical roles.  Quality is everyone’s responsibility, which means the tests themselves need to be easily understood by all stakeholders.

### Tech stack
This is a demo project show how to implement a test fw for Upload file features that using BDD with POM in Selenium python

* Python v4.8.3
* Selenium v4.8.3
* Pycharm 2022.3.3 (Community Edition): IDE's using
* Behave 1.2.6
* Webdriver-Manager v3.8.5
* allure-behave-2.13.1 allure-python-commons-2.13.1 pluggy-1.0.0: use for reporting

### Project Structure
The project uses a standard structure and naming convention:
* `features`  - this folder contains the Gherkin `.feature` files, one per website page. By separating out the tests for each page into separate feature files we continue the POM theme of page independence and make it easier to extend the framework in the future. Each feature file is named after the page it tests, e.g. `upload_file.feature` contains the tests for the Upload page.
* `pages` - the POM implementation of the individual website pages, one class file per page. Each class is named after the corresponding page e.g. `Upload`. Note, the filenames match the page names and do not match the class names exactly. For example, the `Upload` class in the `upload_page.py` file. There is also a `BasePage` which the other page classes implement/extend through inheritance.
* `steps` - a collection of files containing the implementation of the steps from the BDD feature files. As above, there is one steps file per page and each is named after the page under test, e.g. `upload_steps.py`. 
NB Unlike the Java equivalent, there is no Common Steps files containing step definitions that are used by more than one feature file. This means there is some duplication of code across individual steps files at this stage, in particular for verifying the page title as I have declared the related variable and method as abstract in the base page class, meaning each page must define these. This is required as the HTML tag for the page title varies from page to page. Deduplicating these steps is something I have yet to work out how to properly resolve in Python.
* `config.json` - a JSON object used to define certain configuration options such as the browser, whether to run headless and the implicit wait timeout.

### Running tests
Please ensure install and config all Env before running (for each installation and config, please go to their homepages and follow instructions based on your Env (Win, Linux, MAC...))

The tests are easy to run as the project uses Pycharm with Behave BDD, so running the tests is simple to run `upload_file.feature` using behave cmd (e.g: behave .\features\upload_file.feature)
)

Each test opens up in a separate browser instance (which is closed at the end of the test) so is not the fastest way to run a test suite, but it is the right way as we should ensure that tests are wholly independent of one another, do not share state and can run in any order.

### Test Reports
A report is generated for each test run is using Allure report. This is a simple report showing a list of the steps classes (each linked to a feature file) that have been executed and the overall result. In the event of a failing scenario, the details of the failure (actual versus expected result) are shown to allow easy debugging.

### Development plan
Testsuite running: define and run testsuite (e.g: add `BeforeAll` and `AfterAll` hook to control the start and end of each testsuite running.)

Desired capabilities: define the capabilities for each Env support and running on web (Chrome, FF, Edge...) and mobile (Android, iOS).

Report improvement: Based on proj needs, define more info and steps if needed.

CI/CD integration: based on the result of CI/CD plan (mentioned in Test plan), integrate the tests to CI/CD pipeline of DevOps team so whenever new build comes will trigger the related tests.

Other integrations:
* Grafana: for Dashboard 
* Jira: for bugs/user story linking
* ...

Other items based on proj target and team capabilities.


