# evvve-tests
Test task for evvve 


HOW TO EXECUTE TESTS: 

1) clone repo via ui or any variant

2) install requirements.txt from root folder of project (evvve-tests): pip install -r requirements.txt

3) execute from root folder of project (evvve-tests): pytest --webdriver=local --alluredir=allure-results 

HOW TO GET EXCELL REPORT: 

After executing the tests, a test_report.xlsx file will be created in the root folder of project. 
However, I suggest using Allure for better visibility of the test results.


HOW TO INSTALL AND GET ALLURE REPORT (Win): 
FOR ANY SYSTEMS CHECK: https://allurereport.org/docs/install/

1) download and install jdk8 https://www.openlogic.com/openjdk-downloads?field_java_parent_version_target_id=416&field_operating_system_target_id=All&field_architecture_target_id=All&field_java_package_target_id=All

2) update env. variables -> JAVA_HOME: C:\Program Files\OpenLogic\jdk-8.0.422.05-hotspot\

3) download and unpack Allure https://github.com/allure-framework/allure2/releases/tag/2.30.0  (allure-2.30.0.zip)

4) update env. variables -> path & PATH: C:\Users\{user}\allure-2.30.0\allure-2.30.0\bin or just copy/past path from folder

5) check installation in terminal from root: allure --version . output should contains version

6) after execution of tests execute in terminal from root: allure serve {path to allure-results folder in evvve-tests}
