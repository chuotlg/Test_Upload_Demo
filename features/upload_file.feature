Feature: Upload File

    Scenario: Verify successful msg is displayed after uploading a valid file
        Given I launch the chrome browser
        When I open the 'upload file' page
        And I select a valid file to upload
        And I accept the terms
        And I click on Submit btn
        Then a successful msg for uploading the file is displayed
        And close browser
