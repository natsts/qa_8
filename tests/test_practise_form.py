import allure
from allure_commons.types import Severity
from selene.support.shared import browser
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from model.page import practice_form
from utils import attach


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "natsts")
def test_practise_form(size_browser):
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options)

    browser.config.driver = driver

    with allure.step('Ореn practice form'):
        practice_form.open_form()

    with allure.step('Fill all fields'):
        practice_form.fill_contact_fields('Test', 'Testovych', 'test123@mail.ru', '9617778558')
        practice_form.select_gender('Female')
        practice_form.select_year('1996')
        practice_form.select_month('May')
        practice_form.select_day('20')
        practice_form.select_subject('English')
        practice_form.select_hobby('Reading')
        practice_form.add_image('/media/cat.jpg')
        practice_form.add_address('Moscow')
        practice_form.select_state('NCR')
        practice_form.select_city('Delhi')
        practice_form.submit()

    with allure.step('Check header and data'):
        practice_form.check_header('Thanks for submitting the form')
        practice_form.check_data(
            'Test Testovych',
            'test123@mail.ru',
            'Female',
            '9617778558',
            '20 May,1996',
            'English',
            'Reading',
            'cat.jpg',
            'Moscow',
            'NCR Delhi'
        )

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)
