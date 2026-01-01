from pages.enable_disable_page import EnableDisablePage

def test_enable_disable_input(driver):
    enable_disable_page = EnableDisablePage(driver)
    enable_disable_page.open("https://the-internet.herokuapp.com/dynamic_controls")

    enable_disable_page.toogle_input()
    


