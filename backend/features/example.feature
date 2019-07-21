Feature: Users

Scenario Outline: GET User
    Given I create the users
        |name    |job   |
        |Morpheus|leader|   
    When I list user with id <id>
    Then I verify status code <status_code>

    Examples: Positive
    | id | status_code |
    | 1  | 200         |

    Examples: Negative
    |id          |status_code  |
    |arraystrings|404          |

Scenario: GET list users
    Given I create the users
        |name    |job   |
        |Morpheus|leader|
        |Renato  |leader|  
        |Mauricio|leader|  
        |Sei la  |leader|  
    When I list users with page "1"
    Then I verify status code 200

