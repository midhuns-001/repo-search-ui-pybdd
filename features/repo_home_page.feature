Feature: Repo List Home Page

  Background: Open Home page
    Given I have navigated to the 'Repository-List' "Home" page

  @smoke @repo_list_home_page
  Scenario: Verify Repo home page
    Then the page title is "Repository List"
    Then verify repo list table present
    Then verify repo list table columns like name, owner, stars, link, details
    Then verify no data found message in the table
    Then verify default rows per page is listed as 10 in rows per page drop down
    Then verify repo search box is enabled
    Then verify repo search button is present
    Then verify 0 entities are present in the table
    Then verify previous and next buttons are present in the page

  @smoke @regression @repo_list_home_page
  Scenario Outline: List and verify the properties of a git repo in repo table given a name
    Then the page title is "Repository List"
    Then enter <repo_name> in search box
    Then click on search button
    Then verify repo list table columns like name, owner, stars, link, details
    Then verify <no_of_rows> present in table
    Then verify Get Details tooltip for the row <row_name> by mouse hover
Examples:
  | repo_name               | no_of_rows   | row_name        |
  | midhuns-001/midhuns-001 |  7           | python_learning |

  @smoke @regression @repo_list_home_page
  Scenario Outline: List and verify the repo details pop up for a given repo list in the table
    Then the page title is "Repository List"
    Then enter <repo_name> in search box
    Then click on search button
    Then verify repo list table columns like name, owner, stars, link, details
    Then verify <no_of_rows> present in table
    Then click on Get Details icon for <row_name> <repo_name> and verify the repo details pop up
    Then verify the fields in repo details pop up
    Then click on ok button and come back to home page
Examples:
  | repo_name                   | no_of_rows   | row_name        |
  | midhuns-001/ecommerce-ui-fw |  1           | ecommerce-ui-fw |


#Scenario Outline: List and verify the rows per page option given a repo name
    #Then the page title is "Repository List"
    #enter <repo_name> in search box
    #click on search button
    # verify the default raws per page matches with listed rows
    #change the rows per page option and verify the table

#Examples:
 # | repo_name | rows_per_page |
  #| react |    50 |


#Scenario Outline: Verify the previous and next button in the Repo home page


#Scenario Outline: Click and verify link to the github url from repo list home page
