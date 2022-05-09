from abc import ABC, abstractmethod
from selenium.webdriver.common.by import By


class BasePage():
    BASE_URL = "http://localhost:3000/"
    _page_loading_message_xpath = (By.XPATH, "//div[@data-testid='bars-loading']")
    _no_data_found_message_xpath = (By.XPATH, "//h6[text()='No Data Found']")

    PAGE_URLS = {
        "home": BASE_URL,
        # "checkboxes": BASE_URL + "/checkboxes",
        "checkboxes": BASE_URL,
        # "dropdown": BASE_URL + "/dropdown",
        # "dynamic controls": BASE_URL + "/dynamic_controls",
        ##"form authentication": BASE_URL + "/login",
        # "inputs": BASE_URL + "/inputs",
        # "secure area": BASE_URL + "/secure"
    }

    @property
    def PAGE_TITLE(self):
        return (By.XPATH, "//div[contains(@class, 'MuiTypography-root')]")

    @abstractmethod
    def get_page_title_text(self):
        pass

    FORK_LINK = (By.XPATH, "/html/body/div[2]/a")
    FORK_LINK_IMG = (By.XPATH, "/html/body/div[2]/a/img")
    FOOTER = (By.ID, "page-footer")
    FOOTER_LINK = (By.XPATH, "//*[@id=\"page-footer\"]//a")

    def __init__(self, browser):
        self.browser = browser

    