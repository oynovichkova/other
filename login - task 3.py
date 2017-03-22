import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver (request):
    wd = webdriver.Chrome('C:/Python34/Lib/site-packages/selenium/webdriver/common/chromedriver')
    request.addfinalizer (wd.quit)
    return wd

def test_example(driver):
    driver.get("http://localhost/litecart/")
    driver.find_element_by_name("email").send_keys("oly@oly.ru")
    driver.find_element_by_name("password").send_keys("123456")
    driver.find_element_by_name("login").click()
    WebDriverWait(driver,10).until(EC.title_is("Online Store | My Store"))