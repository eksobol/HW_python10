from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_github_issue():
    browser.open("https://github.com/eksobol/HW_python10")

    s("#issues-tab").click()

    s(by.partial_text("Issue for Test")).should(be.visible)
