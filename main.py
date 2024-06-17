from getpass import getpass
from colored import fg


# important variables
normal_color = fg('black')
error_color = fg('red')
success_color = fg('green')
info_color = fg('blue')


# error code
exit_code = False

# patients data in dictionary format
patients_data = {}


while exit_code != True:
    # =========================================> start of program code
    print(info_color + "\n===================================\nWELCOME TO HMS PLEASE REGISTER HERE\n===================================\n")
    # entering patients data on registration
    try:
        patient_username = input(
            normal_color + "Enter your preferred username:\n")
        patient_first_name = input(normal_color + "Enter your first name:\n")
        patient_last_name = input(normal_color + "Enter your last name:\n")
        patient_age = int(input(normal_color + "Enter your age:\n"))
        patient_address = input(normal_color + "Enter your address:\n")
        patient_password = getpass(normal_color + "Enter your password:\n")
        confirm_password = getpass(normal_color + "Confirm password:\n")

        while confirm_password != patient_password:
            print(error_color + "passwords donot match")

            # enable user to retype the password
            patient_password = getpass(
                normal_color + "Enter your new password:\n")
            confirm_password = getpass(normal_color + "Confirm password:\n")
        else:
            patients_data = {
                'username': patient_username,
                'first_name': patient_first_name,
                'last_name': patient_last_name,
                'age': patient_age,
                'address': patient_address,
                'password': patient_password
            }
            print(success_color + 'Registered successfully')
            exit_code = True

    except:
        print(error_color + 'Invalid data entry, please enter correct data format')
