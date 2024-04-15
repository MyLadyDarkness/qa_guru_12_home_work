import datetime

import allure

from data.users import User
from model.pages.registration_page import RegistrationPage


def test_demoqa():
    test_user = User(
        first_name='Oleg',
        last_name='Teplov',
        email='oteplov@gmail.com',
        gender='Other',
        user_number='7123456789',
        birthday=datetime.date(1981, 4, 14),
        subject='Hindi',
        hobby='Reading',
        picture='picture.jpg',
        address='Some address',
        state='NCR',
        city='Noida'
    )

    registration_page = RegistrationPage()

    with allure.step("Open registration page"):
        registration_page.open_page()

    with allure.step("Fill form"):
        registration_page.register(test_user)

    with allure.step("Check filled fields"):
        registration_page.should_have_registered(test_user)
