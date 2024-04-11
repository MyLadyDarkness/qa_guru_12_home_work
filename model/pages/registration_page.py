import os

from selene import have, command
from selene.support.shared import browser


class RegistrationPage:
    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.email = browser.element("#userEmail")
        self.other_gender = browser.element("[for ='gender-radio-3']")
        self.user_number = browser.element("#userNumber")
        self.subject = browser.element('#subjectsInput')
        self.reading_hobby = browser.element("[for ='hobbies-checkbox-2']")
        self.picture = browser.element("#uploadPicture")
        self.address = browser.element("#currentAddress")
        self.state = browser.element('#state')
        self.city = browser.element('#city')

        self.submit_button = browser.element("#submit")

    def open(self):
        browser.open('/automation-practice-form')
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)
        return self

    def fill_first_name(self, value):
        self.first_name.type(value)
        return self

    def fill_last_name(self, value):
        self.last_name.type(value)
        return self

    def fill_email(self, value):
        self.email.type(value)

    def fill_other_gender(self):
        return self.other_gender.click()

    def fill_user_number(self, value):
        return self.user_number.type(value)

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(
            f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)'
        ).click()
        return self

    def fill_subject(self, value):
        return self.subject.type(value).press_enter()

    def fill_reading_hobby(self):
        return self.reading_hobby.click()

    def upload_picture(self):
        return self.picture().send_keys(os.path.abspath("resources/picture.jpg"))

    def fill_address(self, value):
        return self.address.type(value)

    def fill_state(self, name):
        self.state.perform(command.js.scroll_into_view)
        self.state.click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(name)
        ).click()
        return self

    def fill_city(self, name):
        self.city.click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(name)
        ).click()
        return self

    def submit(self):
        return self.submit_button().click()

    def should_registered_user_with(
            self,
            full_name,
            email,
            gender,
            phone,
            birthday,
            subject,
            hobby,
            picture,
            address,
            city
    ):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                full_name,
                email,
                gender,
                phone,
                birthday,
                subject,
                hobby,
                picture,
                address,
                city
            )
        )
        return self
