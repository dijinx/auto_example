from pages.BasePage import BasePage


class ExperimentalPage(BasePage):
    def get_cookie(self):
        cookie = self.driver.get_cookies()
        return cookie
        # BasePage.get_session_cookie(self, 'ssoToken')
