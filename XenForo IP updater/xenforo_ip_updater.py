import json
import os

import requests


def is_number(num):
    try:
        int(num)
        return True
    except ValueError:
        return False


class LoginUpdater:
    def __init__(self):
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        try:
            cred_file = open(os.path.join(__location__, "credentials.json"), "r")
        except FileNotFoundError:
            info = {
                "email": "YourEmailAddress@domain.com",
                "password": "SuperSecureForumsPassword"
            }
            cred_file = open(os.path.join(__location__, "credentials.json"), "w+")
            json.dump(info, cred_file, indent=4)
            print("Please edit the newly created credentials file with your login details and run the script again.")
            quit(0)
            
        creds = json.load(cred_file)
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"}
        self.login_url = "https://mineyourmind.net/forum/login/login"
        self.two_step_url = "https://mineyourmind.net/forum/login/two-step"
        self.request_uri = "/forum/login/two-step?redirect=https%3A%2F%2Fmineyourmind.net%2Fforum%2F&remember=1"
        self.redirect_url = "https://mineyourmind.net/forum/"
        self.login_payload = {
            "login": creds["email"],
            "register": 0,
            "password": creds["password"],
            "remember": 1,
            "cookie_check": 1,
            "xf_token": "",
            "redirect": self.redirect_url
        }
        self.session = requests.Session()
    
    def login(self):
        print("Attempting XenForo Login using provided credentials...")
        # Basically make sure the website knows we're a client, we send a user-agent header to the login page
        self.session.get(url=self.login_url, headers=self.headers)
        # Then we post the login data to the login page.
        response = self.session.post(url=self.login_url, data=self.login_payload)
        parsed_url = response.url.split("?")[0]
        # We got to the two step faze. Ask for the code
        if parsed_url == self.two_step_url:
            print("Website needs you to enter your 2fac auth details. Please type them below and press enter: ")
            two_fac_code = input("> ")
            # Make sure the code is a number. Run this until it is a number
            while not is_number(two_fac_code):
                print("Your two step code must be a number. Please type it again")
                two_fac_code = input("> ")
            print("Sending two fac code to the forums...")
            two_step_payload = {
                "code": int(two_fac_code),
                "provider": "totp",
                "_xfConfirm": 1,
                "_xfToken": "" ,
                "remember": 0,
                "redirect": self.redirect_url,
                "save": "Confirm",
                "_xfRequestUri": self.request_uri,
                "_xfNoRedirect": 1,
                "_xfResponseType": "json",
            }
            # Send the code.
            response2 = self.session.post(self.two_step_url, data=two_step_payload).json()
            # If there is no error in the response and the redirect status is set, the login should have worked.
            if response2.get("error") is None and response2.get("_redirectStatus") is not None:
                redirect = response2["_redirectTarget"]
                print(f"Redirected to: {redirect}. Login should have been successful and your forum IP should be updated!")
            else:
                # Print the response if there was an error.
                print(f"Website Response: {response2}")
        else:
            # Didn't get a 2factor auth URL. Probably okay in most cases but some (like MyM) require two factor on staff accounts.
            print(f"Something may have gone wrong. We expected a 2 factor auth redirect by never got one. Redirected to: {response.url}.")
            print(f"You can try to test if the IP got updated regardless of this fact (sometimes you don't need a two fac code to login.)")


if __name__ == "__main__":
    print("Thanks for using the script!")
    login_updater = LoginUpdater()
    login_updater.login()
