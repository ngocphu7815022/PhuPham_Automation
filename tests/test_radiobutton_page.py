from pages.radiobutton_page import RadioButtonPage

def test_radiobutton_page(driver):
    radio_button_page = RadioButtonPage(driver)
    radio_button_page.open("https://demoqa.com/radio-button")

    radio_button_page.select_yes()
    radio_button_page.select_impressive()

    text_yes = radio_button_page.select_yes()
    text_impressive = radio_button_page.select_impressive()

    print(text_yes)
    print(text_impressive)