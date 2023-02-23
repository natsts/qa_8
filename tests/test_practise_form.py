import allure
from allure_commons.types import Severity
from model.page import practice_form


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "natsts")
@allure.feature("Issue in repository")
@allure.story("Issue 'Issue for allure' has in repository")
@allure.link("https://github.com", name="Testing")
def test_practise_form(size_browser):
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
        practice_form.add_image('\media\cat.jpg')
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
