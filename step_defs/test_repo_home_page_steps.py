from pytest_bdd import scenarios, then, parsers
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


@then('verify the pagination range changed to <rows_per_page>')
@then(parsers.parse('verify the pagination range changed to {rows_per_page}'))
def verify_pagination_range_for_given_rows_per_page(browser, rows_per_page):
    pagination_range_ui = RepoHomePage(browser).get_total_repos_found_in_ui().split(' ')[0].split('–')[1]
    assert pagination_range_ui == rows_per_page


@then('verify previous and next buttons are present in the page')
def verify_previous_next_buttons_in_repo_list_table(browser):
    assert RepoHomePage(browser).get_previous_button_repo_table()
    assert RepoHomePage(browser).get_next_button_repo_table()


@then('verify the table values for a given row <row_name>')
@then(parsers.parse('verify the table values for a given row {row_name}'))
def verify_table_values_for_given_row(browser, row_name):
    assert RepoHomePage(browser).verify_name_field_for_given_row(row_name)
    assert RepoHomePage(browser).verify_owner_field_for_given_row(row_name)
    assert RepoHomePage(browser).verify_stars_field_for_given_row(row_name)
    assert RepoHomePage(browser).verify_link_field_for_given_row(row_name)


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


@then('click on Get Details icon for <row_name> and verify the <message>')
@then(parsers.parse('click on Get Details icon for {row_name} and verify the {message}'))
def click_on_get_details_for_given_repo_name(browser, row_name, message):
    message_ui = RepoHomePage(browser).click_on_get_details_icon(row_name)
    assert message in message_ui


@then('verify empty repo error message')
def verify_empty_repo_error_message(browser):
    RepoHomePage(browser).verify_empty_repo_error_message()


@then('verify the repo details pop up for <repo_name>')
@then(parsers.parse('verify the repo details pop up for {repo_name}'))
def verify_repo_details_pop_up(browser, repo_name):
    assert "Repo Details - " + repo_name == RepoHomePage(browser).get_repo_details_pop_up_header()


@then('verify the fields in repo details pop up')
def verify_repo_details_popup_texts(browser):
    header, value = RepoHomePage(browser).get_last_three_committers_info()
    assert "Last 3 committers:" == header
    header, value = RepoHomePage(browser).get_recent_forked_user()
    assert "Recent Forked User:" == header
    header, value = RepoHomePage(browser).get_recent_forked_user_bio()
    assert "Recent Forked User Bio:" == header


@then('click on <button_option> and come back to home page')
@then(parsers.parse('click on {button_option} and come back to home page'))
def click_ok_button_from_repo_details_pop_up(browser, button_option):
    if 'ok' in button_option.lower():
        RepoHomePage(browser).click_ok_button_from_repo_details_pop_up()
    if 'close' in button_option.lower():
        RepoHomePage(browser).click_close_button_from_repo_details_pop_up()


@then('select the rows per page drop down and update it to <rows_per_page>')
@then(parsers.parse('select the rows per page drop down and update it to {rows_per_page}'))
def select_rows_per_page_from_drop_down(browser, rows_per_page: int):
    RepoHomePage(browser).select_rows_per_page_from_drop_down(rows_per_page)


@then(parsers.parse('click on next button for {iterations} and verify the {message} error message'))
def click_on_next_button_for_iterations(browser, iterations: int, message):
    for i in range(0, int(iterations)):
        message_ui = RepoHomePage(browser).click_and_navigate_to_next_page()
        if 'Success' in message_ui:
            pass
        else:
            break
    assert message in message_ui

@then('click on <button_type> button for no. of <iterations> and verify default rows per page for <rows_per_page>, the table rows less than or equals <rows_per_page> and pagination range')
@then(parsers.parse('click on {button_type} button for no. of {iterations} and verify default rows per page for {rows_per_page}, the table rows less than or equals {rows_per_page} and pagination range'))
def navigate_and_verify_page_properties(browser, button_type, iterations: int, rows_per_page: int):
    button_type_dict = {'next': 'Go to next page', 'previous': 'Go to previous page'}
    if button_type.lower() == 'next':
        end_page_range = int(rows_per_page)
        start_page_range = 1
        start_iter = 0
        end_iter = int(iterations)
    else:
        end_page_range = int(rows_per_page) * (int(iterations) + 1)
        start_page_range = end_page_range - (int(rows_per_page) + 1)
        start_iter = int(iterations)
        end_iter = -1

    for i in range(start_iter, end_iter):
        RepoHomePage(browser).click_and_navigate_to_page(button_type_dict[button_type])

        rows_per_page_ui = RepoHomePage(browser).rows_per_page_in_drop_down()
        assert rows_per_page_ui == rows_per_page

        rows_from_ui = RepoHomePage(browser).get_rows_in_given_page()
        assert rows_from_ui <= int(rows_per_page)
        if button_type.lower() == 'next':
            end_page_range = end_page_range + int(rows_per_page)
            start_page_range = start_page_range + int(rows_per_page)
        else:
            end_page_range = end_page_range + int(rows_per_page)
            start_page_range = end_page_range - (int(rows_per_page) + 1)

        page_range = str(start_page_range) + '–' + str(end_page_range)
        pagination_range_ui = RepoHomePage(browser).get_total_repos_found_in_ui().split(' ')[0]
        assert pagination_range_ui == page_range


@then('click on link <github_link> and verify the url opened in new tab')
@then(parsers.parse('click on link {github_link} and verify the url opened in new tab'))
def click_on_link_and_verify_url(browser, github_link):
    url = RepoHomePage(browser).click_on_link_and_verify_url(github_link)
    assert "https://github.com/" + github_link == url



