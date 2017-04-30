Feature: Test site url
  Scenario: User visits home page
    When user goes to home page
    Then it should have the title 'Continuum'
    Then I enter username and password and click login
    
  