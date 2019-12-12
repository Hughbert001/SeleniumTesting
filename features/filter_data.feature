Feature: Filter data appearing on dashboard 
    Scenario: filter data on dashboard by name 
        Given user is on the dashboard page 
        When user selects a specifc user by name 
        Then the components on the dashboard are search specific 
    Scenario: filter data on dashboard by customer number 
        Given user is on the dashboard page 
        When user selects a specific user by customer number 
        Then the components on the dashboard are search specific