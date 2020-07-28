import auto
import yaml

def err():
    print("please message me the error you received")

def deserializer():
    with open(r'example.yml') as file:
        user = yaml.full_load(file)
    return user

if __name__ == "__main__":
    user = deserializer()
    helper=auto.Driver("C:\Program Files\chromedriver_win32\chromedriver.exe")  
    if(helper.signIn(user["email"],user["pwd"])):
        if(helper.joinMeeting()):
            pass
        else:
            err()

    else:
        err()
    