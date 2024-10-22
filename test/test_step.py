from allure_commons.types import Severity
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
import allure


def test_github_issue():
    allure.dynamic.tag("web")
    allure.dynamic.severity(Severity.MINOR)
    allure.dynamic.feature("Проверить issue")
    allure.dynamic.story("Имя issue")
    allure.dynamic.link("https://github.com", name="test")

    with allure.step("Открываем страницу пользователя"):
        browser.open("https://github.com/eksobol/HW_python10")

    with allure.step("Ищем issues"):
        s("#issues-tab").click()

    with allure.step("Проверяем текст"):
        s(by.partial_text("Issue for Test")).should(be.visible)
