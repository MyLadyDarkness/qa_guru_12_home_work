import os
import os.path

from selene import have, command
from selene.support.shared import browser


class RegistrationPage:

    def open_page(self):
        browser.open('/automation-practice-form')
        return self

    def picture(self, user_photo):
        root_path = os.getcwd()
        return os.path.join(root_path, f"resources\\{user_photo}")

    def register(self, test_user):
        browser.element('#firstName').type(test_user.first_name)
        browser.element('#lastName').type(test_user.last_name)
        browser.element('#userEmail').type(test_user.email)
        browser.element('[for="gender-radio-3"]').click()
        browser.element('#userNumber').type(test_user.user_number)
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').type(test_user.birthday.year)
        browser.element('.react-datepicker__month-select').type(test_user.birthday.month)
        browser.element(f'.react-datepicker__day--0{test_user.birthday.day}').click()
        browser.element('#subjectsInput').type(test_user.subject).press_enter()
        browser.element('[for="hobbies-checkbox-2"]').click()
        browser.element('#uploadPicture').send_keys(self.picture("picture.jpg"))  # (resource.path(test_user.photo))
        browser.element('#currentAddress').type(test_user.address)
        browser.element('#react-select-3-input').type(test_user.state).press_enter()
        browser.element('#react-select-4-input').type(test_user.city).press_enter()
        browser.element('#submit').perform(command.js.scroll_into_view).click()

    def should_have_registered(self, test_user):
        browser.element('.table').all('tr td:nth-child(2)').should(have.texts(
            f'{test_user.first_name} {test_user.last_name}',
            test_user.email,
            test_user.gender,
            test_user.user_number,
            f'{test_user.birthday.strftime("%B")}',
            test_user.subject,
            test_user.hobby,
            test_user.picture,
            test_user.address,
            f'{test_user.state} {test_user.city}'
        ))
