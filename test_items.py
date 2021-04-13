from time import sleep

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_basket_button_must_present(browser):
    browser.get(link)
    sleep(30)
    assert browser.find_element_by_css_selector("button.btn-add-to-basket"), f'Button "Add to basket" is not found'
