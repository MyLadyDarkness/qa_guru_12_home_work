from model.pages.registration_page import RegistrationPage


def test_demoqa():
    registration_page = RegistrationPage()
    registration_page.open()

    registration_page.fill_first_name("Oleg")
    registration_page.fill_last_name("Teplov")

    registration_page.fill_email("oteplov@gmail.com")
    registration_page.fill_other_gender()
    registration_page.fill_user_number("7123456789")

    registration_page.fill_date_of_birth(1981, 3, 14)
    registration_page.fill_subject("Hindi")
    registration_page.fill_reading_hobby()
    registration_page.upload_picture("picture.jpg")
    registration_page.fill_address("Some address")
    registration_page.fill_state("NCR")
    registration_page.fill_city("Noida")

    registration_page.submit()

    registration_page.should_registered_user_with(
        'Oleg Teplov',
        'oteplov@gmail.com',
        'Other',
        '7123456789',
        '14 April,1981',
        'Hindi',
        'Reading',
        'picture.jpg',
        'Some address',
        'NCR Noida',
    )
