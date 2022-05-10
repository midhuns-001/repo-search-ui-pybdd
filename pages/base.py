from abc import abstractmethod
from selenium.webdriver.common.by import By


class BasePage:
    BASE_URL = "http://localhost:3000/"
    _page_loading_message_xpath = (By.XPATH, "//div[@data-testid='bars-loading']")
    _no_data_found_message_xpath = (By.XPATH, "//h6[text()='No Data Found']")

    PAGE_URLS = {
        "home": BASE_URL
    }

    @property
    def PAGE_TITLE(self):
        return (By.XPATH, "//div[contains(@class, 'MuiTypography-root')]")

    @abstractmethod
    def get_page_title_text(self):
        pass

    def __init__(self, browser):
        self.browser = browser

    