  @runSearch
  Feature: Python Nordeste Search Event
    Scenario Outline: Search existing definition of <searchTxt> word
      Given I open: https://en.wiktionary.org/prepare by the first time
      When I am on homepage
      Then I look up the definition of the word <searchTxt>

      Examples: searchbase
        | searchTxt |                                                                         
        | apple     |

    