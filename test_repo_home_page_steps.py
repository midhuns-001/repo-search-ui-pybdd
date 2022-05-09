import time
from pytest_bdd import scenarios, when, then, parsers
from pages.repo_home_page import RepoHomePage

scenarios('../features/repo_home_page.feature')


@then(parsers.parse('the page title is "{title}"'))
def verify_page_title(browser, title):
    assert title == RepoHomePage(browser).get_page_title_text()


@then('verify repo list table present')
def verify_repo_list_table(browser):
    assert RepoHomePage(browser).check_repo_list_table_element()


@then(parsers.parse('verify repo list table columns like {column_names}'))
def verify_column_names(browser, column_names):
    column_list = column_names.split(', ')
    print(column_list)
    for col in column_list:
        assert RepoHomePage(browser).check_repo_table_column(col)


@then('verify no data found message in the table')
def verify_no_data_found_message(browser):
    assert RepoHomePage(browser).get_no_data_found_message()


@then(parsers.parse('verify default rows per page is listed as {no_of_rows} in rows per page drop down'))
def get_rows_per_page(browser, no_of_rows):
    rows_per_page = RepoHomePage(browser).rows_per_page_in_drop_down()
    assert no_of_rows == rows_per_page


@then('verify repo search box is enabled')
def verify_repo_name_search_box(browser):
    assert RepoHomePage(browser).get_repo_name_search_box()


@then('verify repo search button is present')
def verify_repo_search_button(browser):
    assert RepoHomePage(browser).get_repo_search_button()


@then('verify <rows> entities are present in the table')
@then(parsers.parse('verify {rows} entities are present in the table'))
def verify_num_of_entities_present_in_table(browser, rows: int):
    total_rows_in_ui = RepoHomePage(browser).get_total_repos_found_in_ui().split(' ')[-1]
    assert rows == total_rows_in_ui


@then('verify previous and next buttons are present in the page')
def verify_previous_next_buttons_in_repo_list_table(browser):
    assert RepoHomePage(browser).get_previous_button_repo_table()
    assert RepoHomePage(browser).get_next_button_repo_table()


@then('enter <repo_name> in search box')
@then(parsers.parse('enter {repo_name} in search box'))
def enter_repo_name_to_be_searched(browser, repo_name):
    RepoHomePage(browser).enter_repo_name_to_be_searched(repo_name)


@then('click on search button')
def click_search_button(browser):
    RepoHomePage(browser).click_search_button()


@then('verify <no_of_rows> present in table')
@then(parsers.parse('verify {no_of_rows} present in table'))
def verify_no_of_rows_present_in_table(browser, no_of_rows: int):
    rows_from_ui = RepoHomePage(browser).get_rows_in_given_page()
    assert int(no_of_rows) == rows_from_ui


@then('verify Get Details tooltip for the row <row_name> by mouse hover')
@then(parsers.parse('verify Get Details tooltip for the row {row_name} by mouse hover'))
def verify_details_tooltip_by_mouse_hover(browser, row_name):
    tooltip_message_ui = RepoHomePage(browser).get_tooltip_message_from_row_name(row_name)
    assert tooltip_message_ui == 'Get Details'


@then('click on Get Details icon for <row_name> <repo_name> and verify the repo details pop up')
@then(parsers.parse('click on Get Details icon for {row_name} {repo_name} and verify the repo details pop up'))
def click_on_get_details_for_given_repo_name(browser, row_name, repo_name):
    assert "Repo Details - " + repo_name == RepoHomePage(browser).click_on_get_details_icon(row_name)


@then('verify the fields in repo details pop up')
def verify_repo_details_popup_texts(browser):
    header, value = RepoHomePage(browser).get_last_three_committers_info()
    assert "Last 3 committers:" == header
    header, value = RepoHomePage(browser).get_recent_forked_user()
    assert "Recent Forked User:" == header
    header, value = RepoHomePage(browser).get_recent_forked_user_bio()
    assert "Recent Forked User Bio:" == header


@then('click on ok button and come back to home page')
def click_ok_button_from_repo_details_pop_up(browser):
    RepoHomePage(browser).click_ok_button_from_repo_details_pop_up()
