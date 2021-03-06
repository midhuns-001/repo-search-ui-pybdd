Feature: Repo List Home Page

  Background: Open Home page
    Given I have navigated to the 'Repository-List' "Home" page

  @smoke @repo_list_home_page
  Scenario: Verify Repo home page and its properties
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
    Then verify the table values for a given row <row_name>
  Examples:
    | repo_name               | no_of_rows   | row_name        |
    | midhuns-001/midhuns-001 |  7           | python_learning |

  @regression @repo_list_home_page
  Scenario Outline: List and verify the repo details pop up for a given repo list in the table
    Then the page title is "Repository List"
    Then enter <repo_name> in search box
    Then click on search button
    Then verify repo list table columns like name, owner, stars, link, details
    Then verify <no_of_rows> present in table
    Then click on Get Details icon for <row_name> and verify the <message>
    Then verify the repo details pop up for <repo_name>
    Then verify the fields in repo details pop up
    Then click on <button_option> and come back to home page
  Examples:
    | repo_name                   | no_of_rows   | row_name        | message      | button_option |
    | midhuns-001/ecommerce-ui-fw |  1           | ecommerce-ui-fw | Repo Details | ok            |
    | midhuns-001/ecommerce-ui-fw |  1           | ecommerce-ui-fw | Repo Details | close         |


  @regression @repo_list_home_page
  Scenario Outline: List and verify the rows per page drop down given a repo name
    Then the page title is "Repository List"
    Then enter <repo_name> in search box
    Then click on search button
    Then verify repo list table columns like name, owner, stars, link, details
    Then verify default rows per page is listed as 10 in rows per page drop down
    Then select the rows per page drop down and update it to <rows_per_page>
    Then verify default rows per page is listed as <rows_per_page> in rows per page drop down
    Then verify <rows_per_page> present in table
    Then verify the pagination range changed to <rows_per_page>
  Examples:
    | repo_name | rows_per_page |
    | react     |    10         |
    | react     |    25         |
    | react     |    50         |

  @regression @repo_list_home_page
  Scenario Outline: Navigate to next page and verify the repo table properties. Verify previous pages once its done
    Then the page title is "Repository List"
    Then enter <repo_name> in search box
    Then click on search button
    Then verify repo list table columns like name, owner, stars, link, details
    Then select the rows per page drop down and update it to <rows_per_page>
    Then verify default rows per page is listed as <rows_per_page> in rows per page drop down
    Then verify <rows_per_page> present in table
    Then click on next button for no. of <iterations> and verify default rows per page for <rows_per_page>, the table rows less than or equals <rows_per_page> and pagination range
    Then click on previous button for no. of <iterations> and verify default rows per page for <rows_per_page>, the table rows less than or equals <rows_per_page> and pagination range

  Examples:
    | repo_name | rows_per_page | iterations |
    | react     |    10         | 1          |
    | react     |    25         | 2          |
    | react     |    50         | 3          |

  @regression @repo_list_home_page
  Scenario Outline: Click and verify link to the github url from repo list home page
    Then the page title is "Repository List"
    Then enter <repo_name> in search box
    Then click on search button
    Then verify repo list table columns like name, owner, stars, link, details
    Then verify <no_of_rows> present in table
    Then click on link <github_link> and verify the url opened in new tab
  Examples:
    | repo_name               | no_of_rows   | github_link                |
    | midhuns-001/midhuns-001 |  7           | midhuns-001/python_learning |

  @regression @repo_list_home_page
  Scenario Outline: Verify the repo details error message for a repo which is empty - Negative
    Then the page title is "Repository List"
    Then enter <repo_name> in search box
    Then click on search button
    Then verify repo list table columns like name, owner, stars, link, details
    Then verify <no_of_rows> present in table
    Then click on Get Details icon for <row_name> and verify the <message>
  Examples:
    | repo_name    | no_of_rows   | row_name    | message                 |
    | midhuns-001  |  1           | midhuns-001 | Git Repository is empty |


  @regression @repo_list_home_page
  Scenario Outline: Navigate to subsequent pages of a repo and verify the api rate limit error message
    Then the page title is "Repository List"
    Then enter <repo_name> in search box
    Then click on search button
    Then verify repo list table columns like name, owner, stars, link, details
    Then select the rows per page drop down and update it to <rows_per_page>
    Then verify default rows per page is listed as <rows_per_page> in rows per page drop down
    Then verify <rows_per_page> present in table
    Then click on next button for <iterations> and verify the api rate limit exceeded error message
  Examples:
    | repo_name | rows_per_page | iterations |
    | java      |    50         | 50         |