Structure-

- Tests are designed using Behave BDD and Python Requests package.
- This project is a standard Python project
- Feature file is present at /API_Automation_Crypto/features folder

How to Run- 

- Clone this repository from github, import it to Pycharm (or any other IDE).
- To execute the feature file run "behave --no-capture" from terminal
  - To view the reports alongside run, please follow below steps:
    - Download allure
    - run behave --no-capture -f allure_behave.formatter:AllureFormatter -o AllureReports from terminal
    - Above command will create a Json file in AllureReports folder of the project
    - Run allure serve {path of Json}


Improvements:

- Tests are currently running sequentially, some changes may required to run them in parallel
- Logging can be added.


