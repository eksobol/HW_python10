from allure_commons.types import Severity
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
import allure


@allure.tag("web")
@allure.severity(Severity.MINOR)
@allure.label("owner", "eksobol")
@allure.feature("Проверить issue")
@allure.story("Имя issue")
@allure.link("https://github.com", name="test")
def test_issue():
    github_open()
    search_issue()
    check_text()


@allure.step("Открываем главную страницу")
def github_open():
    browser.open("https://github.com/eksobol/HW_python10")


@allure.step("Ищем issues")
def search_issue():
    s("#issues-tab").click()


@allure.step("Проверяем текст")
def check_text():
    s(by.partial_text("Issue for Test")).should(be.visible)
