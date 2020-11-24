import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_button_add_in_basket(browser):
    browser.get(link)
    assert browser.find_element_by_css_selector(".btn.btn-lg.btn-primary.btn-add-to-basket")