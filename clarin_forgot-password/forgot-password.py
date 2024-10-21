import random

def is_valid_email(email):
    return "@cit.edu" in email or "@gmail.com" in email

def send_code():
    return random.randint(1000, 9999)

def is_valid_password(password):
    if len(password) >= 6:
        return True
    else:
        return False

class ForgotPasswordStates:
    # State 1: Email Input
    # State 2: Code Verification
    # State 3: Reset Password
    # State 4: Trying Login
    # State 5: Login Success
    # State 6: Login Failed

    def __init__(self):
        self.state = "State 1"
        self.verification_code = None
        self.email = None
        self.new_password = None

    def process_state(self):
        print("_____________________________________________________")
        print("\nName and Section:\n| Jake R. Clarin - F2\n")
        print("About the Program:\n| This program shows the state transitions of the entire process of forgetting a password as you change your old password to a new one.")
        print("_____________________________________________________")
        
        while self.state != "State 5":
            if self.state == "State 1":
                self.email = input("\n[ FORGET YOUR PASSWORD ]\n\nEnter your email address: ")

                if is_valid_email(self.email):
                    self.verification_code = send_code()
                    print(f"| Verification code has been sent to {self.email} (Code: {self.verification_code})")
                    print("_____________________________________________________")
                    self.state = "State 2"

                else:
                    print("| Invalid email format. Please try again.")
                    print("_____________________________________________________")

            elif self.state == "State 2":
                code_input = input("\n[ VERIFICATION CODE ]\n\nEnter the verification code: ")

                if code_input.isdigit() and int(code_input) == self.verification_code:
                    print("| The code has been successfully verified!")
                    print("_____________________________________________________")
                    self.state = "State 3"

                else:
                    print("| Incorrect verification code. Please try again.")
                    print("_____________________________________________________")

            elif self.state == "State 3":
                self.new_password = input("\n[ NEW PASSWORD ]\n\nEnter your new password (min 6 char): ")

                if is_valid_password(self.new_password):
                    print("| Password has been reset successfully!")
                    print("_____________________________________________________")
                    self.state = "State 4"

                else:
                    print("| Password must be at least 6 characters long. Please try again.")
                    print("_____________________________________________________")

            elif self.state == "State 4":
                login_email = input("\n[ LOG IN TO ACCOUNT ]\n\nEnter your email: ")
                login_password = input("Enter your password: ")

                if login_email == self.email and login_password == self.new_password:
                    print("\n| You have successfully login!")
                    print("_____________________________________________________")
                    self.state = "State 5"

                else:
                    self.state = "State 6"
                    print("\n| You have entered an invalid email or password. Please try again.")
                    print("_____________________________________________________")

                    retry = input("\nWould you like to reset your password again or try again? (yes/no): ").strip().lower()

                    if retry == "yes":
                        print("_____________________________________________________")
                        self.reset()
                    else:
                        print("_____________________________________________________")
                        self.state = "State 4"
        
    def reset(self):
        self.state = "State 1"
        self.verification_code = None
        self.email = None
        self.new_password = None

app = ForgotPasswordStates()
app.process_state()