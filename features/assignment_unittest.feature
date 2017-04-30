Feature: CRUD operations on  Assignment
	Scenario: Creating a new assignment
		When I go to create assignment page
		Then I should be able to create an assignment
	
	Scenario: Retriving saved assignments
		When I go to list assignment page
		Then assignment saved should be present



	
