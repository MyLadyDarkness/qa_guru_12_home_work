import datetime

from data.users import User
from model.pages.registration_page import RegistrationPage
from utils import attach
from selene import browser, have, command

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
    registration_page.open_page()
    registration_page.register(test_user)

    registration_page.should_have_registered(test_user)

# attach.add_html(browser)
# attach.add_screenshot(browser)
# attach.add_logs(browser)