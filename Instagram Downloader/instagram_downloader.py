import requests
import shutil
import re
import json

print("-" * 25)
print("\nThanks for using this script. Note: Videos will not be downloaded and must be downloaded via the link this script provides (should be easy enough to figure out :wink:). Images will be downloaded as \"output.jpg\"\n")
print("-" * 25)
user_type = input("Image or Video? (I or V): ")
user_type = user_type.lower()
user_input = input("Provide an instagram post link please: ")
headers = {
        "cookie": "none"
    }
if headers["cookie"] == 'none':
    print("Cookie is not set. Private pictures and videos will not work!")
    print("Please obtain cookie by looking in the Chrome developer tools and then under the Application tab or alternatively obtain your cookie from your instagram network traffic when loading the instagram webpage")
    print("Then all you need to do is edit the \"headers\" variable above with your cookie info.")
    headers = {}
        
if user_type == "i":
    url = f"{user_input}media/?size=l"
    req = requests.get(url, headers=headers)
    if req.history:
        img = requests.get(req.url, stream=True)
        outfile = open("output.jpg", "wb")
        # To decode the size of the image so the file actually has a size when we write it
        img.raw.decode_content = True
        # Write the bytes to the file
        shutil.copyfileobj(img.raw, outfile)
        # Delete the image from memory.
        del req
        del img
    else:
        print("Account may be private.")

if user_type == "v":
    req = requests.get(user_input, headers=headers)
    for line in req.text.split("\n"):
        l = line.strip()
        test = re.match('<script type="text/javascript">window.__initialDataLoaded', l)
        if test is not None:
            l = l.split(",", 1)[1] \
                 .replace("true", "1") \
                 .replace("false", "0") \
                 .strip(");</script><script type=\"text/javascript\"")
            try:
                test2 = json.loads(l)
                print("Video URL: " + test2["graphql"]["shortcode_media"]["video_url"])
                exit(0)
            except json.JSONDecodeError as e:
                print("Cannot parse JSON from payload. Instagram may have changed their site to stop this link gathering method. Error: ")
                print(e)
                exit(1)
    print("Account may be private")