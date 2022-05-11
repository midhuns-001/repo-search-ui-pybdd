import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base import BasePage


class RepoHomePage(BasePage):

    _repo_list_table_xpath = (By.XPATH, "//div[contains(@class, 'MuiTableContainer-root')]")
    _repo_list_table_name_column_xpath = (By.XPATH, "//table//thead/tr//th[text()='Name']")
    _repo_list_table_owner_column_xpath = (By.XPATH, "//table//thead/tr//th[text()='Owner']")
    _repo_list_table_stars_column_xpath = (By.XPATH, "//table//thead/tr//th[text()='Stars']")
    _repo_list_table_link_column_xpath = (By.XPATH, "//table//thead/tr//th[text()='Link']")
    _repo_list_table_details_column_xpath = (By.XPATH, "//table//thead/tr//th[text()='Details']")

    _repo_list_search_box_text_xpath = (By.XPATH, "//input[@aria-label='search']")
    _repo_list_search_button_xpath = (By.XPATH, "//button[@aria-label='search']")

    _repo_list_rows_per_page_text_field = (By.XPATH, "//p[text()='Rows per page:']")
    _repo_list_rows_select_drop_down_xpath = (By.ID, "mui-1")
    _repos_displayed_rows = (By.XPATH, "//p[contains(@class, 'MuiTablePagination')][2]")
    _repos_button_previous_page_xpath = (By.XPATH, "//button[@aria-label='Go to previous page']")
    _repos_button_next_page_xpath = (By.XPATH, "//button[@title='Go to next page']")

    _repos_table_rows_xpath = (By.XPATH, "//table/tbody//tr")
    _repo_get_details_tooltip_xpath = (By.XPATH, "//div[@role='tooltip']")
    _repo_details_pop_up_header_id = (By.ID, 'customized-dialog-title')
    _repo_details_last_three_committers_header = (By.XPATH, "//p[contains(@class, 'MuiTypography-root')][1]")
    _repo_details_last_three_committers_value = (By.XPATH, "//p[contains(@class, 'MuiTypography-root')][2]")
    _repo_details_recent_forked_user_header = (By.XPATH, "//p[contains(@class, 'MuiTypography-root')][3]")
    _repo_details_recent_forked_user_value = (By.XPATH, "//p[contains(@class, 'MuiTypography-root')][4]")
    _repo_details_recent_forked_user_bio_header = (By.XPATH, "//p[contains(@class, 'MuiTypography-root')][5]")
    _repo_details_recent_forked_user_bio_value = (By.XPATH, "//p[contains(@class, 'MuiTypography-root')][6]")
    _repo_details_ok_button_xpath = (By.XPATH, "//div[contains(@class, 'MuiDialogActions-root')]//button")
    _repo_details_close_button_xpath = (By.XPATH, "//button[@aria-label='close']")

    _repo_details_error_message_pop_up_id = (By.ID, "swal2-title")
    _repo_table_header_no_data_found_message_xpath = (By.XPATH, "//h6[text()='No Data Found']")

    def __init__(self, browser):
        self.browser = browser

    def get_page_title_text(self):
        return self.browser.find_element(*self.PAGE_TITLE).text

    def check_repo_list_table_element(self):
        return self.browser.find_element(*self._repo_list_table_xpath).is_displayed()

    def check_repo_table_column(self, column):
        repo_column_name_xpath = (By.XPATH, "//table//thead/tr//th[text()='" + column.capitalize() + "']")
        return self.browser.find_element(*repo_column_name_xpath).is_displayed()

    def get_no_data_found_message(self):
        return self.browser.find_element(*self._no_data_found_message_xpath).is_displayed()

    def rows_per_page_in_drop_down(self):
        return self.browser.find_element(*self._repo_list_rows_select_drop_down_xpath).text

    def get_repo_name_search_box(self):
        return self.browser.find_element(*self._repo_list_search_box_text_xpath).is_displayed()

    def get_repo_search_button(self):
        return self.browser.find_element(*self._repo_list_search_button_xpath).is_displayed()

    def get_total_repos_found_in_ui(self):
        return self.browser.find_element(*self._repos_displayed_rows).text

    def get_previous_button_repo_table(self):
        return self.browser.find_element(*self._repos_button_previous_page_xpath).is_displayed()

    def get_next_button_repo_table(self):
        return self.browser.find_element(*self._repos_button_next_page_xpath).is_displayed()

    def enter_repo_name_to_be_searched(self, repo_name):
        self.browser.find_element(*self._repo_list_search_box_text_xpath).send_keys(repo_name)

    def click_search_button(self):
        self.browser.find_element(*self._repo_list_search_button_xpath).click()
        WebDriverWait(self.browser, 5).until(EC.invisibility_of_element(self._page_loading_message_xpath))

    def get_rows_in_given_page(self):
        return len(self.browser.find_elements(*self._repos_table_rows_xpath))

    def get_tooltip_message_from_row_name(self, row_name):
        get_details_xpath = (By.XPATH, "//tr//td[text()='" + row_name + "']/ancestor::tr//td[5]//span[@aria-label='Get Details']")
        ActionChains(self.browser).move_to_element(self.browser.find_element(*get_details_xpath)).perform()
        time.sleep(1)
        return self.browser.find_element(*self._repo_get_details_tooltip_xpath).text

    def click_on_get_details_icon(self, row_name):
        get_details_xpath = (By.XPATH, "//tr//td[text()='" + row_name + "']/ancestor::tr//td[5]//span[@role='button']")
        ActionChains(self.browser).move_to_element(self.browser.find_element(*get_details_xpath)).perform()
        try:
            self.browser.find_element(*get_details_xpath).click()
            time.sleep(1)
            if self.browser.find_element(*self._repo_details_error_message_pop_up_id).is_displayed():
                return self.verify_repo_details_pop_up_error_message()
            WebDriverWait(self.browser, 3).until(EC.visibility_of_element_located(self._repo_details_pop_up_header_id))
            if self.browser.find_element(*self._repo_details_pop_up_header_id).is_displayed():
                return self.browser.find_element(*self._repo_details_pop_up_header_id).text
        except:
            self.browser.find_element(*get_details_xpath).click()
            WebDriverWait(self.browser, 3).until(EC.visibility_of_element_located(self._repo_details_pop_up_header_id))
            return self.browser.find_element(*self._repo_details_pop_up_header_id).text

    def verify_repo_details_pop_up_error_message(self):
        return self.browser.find_element(*self._repo_details_error_message_pop_up_id).text

    def get_repo_details_pop_up_header(self):
        WebDriverWait(self.browser, 3).until(EC.visibility_of_element_located(self._repo_details_pop_up_header_id))
        return self.browser.find_element(*self._repo_details_pop_up_header_id).text

    def get_last_three_committers_info(self):
        return self.browser.find_element(*self._repo_details_last_three_committers_header).text, \
               self.browser.find_element(*self._repo_details_last_three_committers_value).text

    def get_recent_forked_user(self):
        return self.browser.find_element(*self._repo_details_recent_forked_user_header).text, \
                self.browser.find_element(*self._repo_details_recent_forked_user_value)

    def get_recent_forked_user_bio(self):
        return self.browser.find_element(*self._repo_details_recent_forked_user_bio_header).text, \
                self.browser.find_element(*self._repo_details_recent_forked_user_bio_value)

    def click_ok_button_from_repo_details_pop_up(self):
        self.browser.find_element(*self._repo_details_ok_button_xpath).click()
        WebDriverWait(self.browser, 1).until(EC.visibility_of_element_located(self.PAGE_TITLE))

    def click_close_button_from_repo_details_pop_up(self):
        self.browser.find_element(*self._repo_details_close_button_xpath).click()
        WebDriverWait(self.browser, 1).until(EC.visibility_of_element_located(self.PAGE_TITLE))

    def select_rows_per_page_from_drop_down(self, rows_per_page):
        self.browser.find_element(*self._repo_list_rows_select_drop_down_xpath).click()
        select_option_xpath = (By.XPATH, "//li[@data-value='" + rows_per_page + "']")
        self.browser.find_element(*select_option_xpath).click()
        WebDriverWait(self.browser, 5).until(EC.invisibility_of_element(self._page_loading_message_xpath))
        time.sleep(2)

    def click_and_navigate_to_page(self, button):
        _repos_navigate_button_xpath = (By.XPATH, "//button[@title='" + button + "']")
        ActionChains(self.browser).move_to_element(self.browser.find_element(*_repos_navigate_button_xpath)).perform()
        self.browser.find_element(*_repos_navigate_button_xpath).click()
        try:
            WebDriverWait(self.browser, 5).until(EC.invisibility_of_element(self._page_loading_message_xpath))
        except:
            self.browser.find_element(*_repos_navigate_button_xpath).click()
            WebDriverWait(self.browser, 5).until(EC.invisibility_of_element(self._page_loading_message_xpath))

    def click_and_navigate_to_next_page(self):
        _repos_navigate_button_xpath = (By.XPATH, "//button[@title='Go to next page']")
        ActionChains(self.browser).move_to_element(self.browser.find_element(*_repos_navigate_button_xpath)).perform()
        self.browser.find_element(*_repos_navigate_button_xpath).click()
        time.sleep(2)
        if self.browser.find_element(*self._repo_table_header_no_data_found_message_xpath).is_displayed():
            return self.verify_repo_details_pop_up_error_message()

        return 'Success'

    def click_on_link_and_verify_url(self, github_link):
        handle_orig = self.browser.current_window_handle
        _repos_link_xpath = (By.XPATH, "//td//a[text()='" + github_link + "']")
        self.browser.find_element(*_repos_link_xpath).click()
        time.sleep(2)
        self.browser.switch_to.window(self.browser.window_handles[1])
        return self.browser.current_url

    def verify_name_field_for_given_row(self, row_name):
        name_field_xpath = (By.XPATH, "//tr//td[text()='" + row_name + "']/ancestor::tr//td[1]")
        return self.browser.find_element(*name_field_xpath).text

    def verify_owner_field_for_given_row(self, row_name):
        owner_field_xpath = (By.XPATH, "//tr//td[text()='" + row_name + "']/ancestor::tr//td[2]")
        return self.browser.find_element(*owner_field_xpath).text

    def verify_stars_field_for_given_row(self, row_name):
        stars_field_xpath = (By.XPATH, "//tr//td[text()='" + row_name + "']/ancestor::tr//td[3]")
        return self.browser.find_element(*stars_field_xpath).text

    def verify_link_field_for_given_row(self, row_name):
        link_field_xpath = (By.XPATH, "//tr//td[text()='" + row_name + "']/ancestor::tr//td[4]//a")
        return self.browser.find_element(*link_field_xpath).text


