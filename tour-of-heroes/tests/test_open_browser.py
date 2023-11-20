from time import sleep

import pytest
from unittest import TestCase

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestOpenBrowser(TestCase):
    @classmethod
    def setUp(cls) -> None:
        super().setUpClass()
        try:
            cls.driver = webdriver.Chrome()
        except:
            super().tearDownClass()
            raise
        return
    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
        return 
    
    def _click_on_hero(self) -> None:
        hero_button = self.driver.find_element(By.XPATH, "/html/body/app-root/app-heroes/ul/li[1]/button")
        hero_button.click()

        
        # try:
        element = WebDriverWait(self.driver, 2).until(
            EC.presence_of_element_located((By.TAG_NAME, "app-hero-detail"))
        )
        self.assertEqual(element.tag_name, "app-hero-detail")
        # finally:
        #     raise RuntimeError(f"Unable to find: app-hero-detail element")

    def test_open_browser(self) -> None:
        self.driver.get("http://localhost:4200")
        self.assertEqual(self.driver.title, "Frontend")
        sleep(1)
        self._click_on_hero()
        sleep(3)

        return 
    