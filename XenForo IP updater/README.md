# XenForo forum IP Updater
Used to update your recent IP address on the MyM forums to stop the two fac auth error that Staff get

See [usage](#usage) for more info on how to use it.

## Usage
1. Run the script using `python xenforo_ip_updater.py` to generate a blank credentials file. Please fill in the email and password for your account in that file and keep it safe!
2. Run the script again and follow the prompts (should ask for 2 factor auth code for MyM forums)

### Notes
If you get redirected to the login page when trying to login, you may have typed your credentials incorrectly. Also make sure that if you are using this for other XenForo forums that all the respective URLs are correct for that forum (two fac url, formatted redirect URI and redirect URL) and that the forum owners allow for users to login automatically like this.