# -*- coding: utf-8 -*-
import unittest

from selenium import webdriver

class pchoutai(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        self.base_url = "http://osapi.t.daniujiaoyu.org/Account/Login?ReturnUrl=%2Fconnect%2Fauthorize%2Fcallback%3Fclient_id%3DWebAdminClient%26redirect_uri%3Dhttp%253A%252F%252Fosui.t.daniujiaoyu.org%252Foidc%252Flogin-callback.html%26response_type%3Did_token%2520token%26scope%3Dopenid%2520profile%2520MvcAdminApi%2520StoreApi%26state%3D6a1eb244ce85410eb2c79996b8a3cba1%26nonce%3D341b96098d104a2b8d0dad1deda4998d"
        self.verificationErrors = []
        self.accept_next_alert = True