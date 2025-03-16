from step_objects.page import RegistrationPage


def test_submit_form():
    registration_form = RegistrationPage()

    registration_form.open()
    registration_form.first_name('Julia')
    registration_form.second_name('Furmanova')
    registration_form.mail_name('ula555@mail.ru')
    registration_form.gender_name()
    registration_form.number_name('3123213131')
    registration_form.birthday_data('8', '1999', '15')
    registration_form.subject_name('Math', 'English')
    registration_form.hobbies_name()
    registration_form.picture_png()
    registration_form.addres_name('Komsomolskaya 191')

    registration_form.ready()

    registration_form.assert_filled_labels('Label Values')
    registration_form.assert_filled_names('Student Name Julia Furmanova')
    registration_form.assert_filled_emaily('Student Email ula555@mail.ru')
    registration_form.assert_filled_gender('Gender Male')
    registration_form.assert_filled_mobile('Mobile 3123213131')
    registration_form.assert_filled_birt('Date of Birth 15 September,1999')
    registration_form.assert_filled_subject('Subjects Maths, English')
    registration_form.assert_filled_hobbies('Hobbies Sports')
    registration_form.assert_filled_picrure('Picture picture.png')
    registration_form.assert_filled_Adress('Address Komsomolskaya 191')
    registration_form.assert_filled_state('State and City NCR Delhi')
