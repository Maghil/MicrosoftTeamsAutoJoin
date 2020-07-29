import auto
import yaml
import time

def err():
    print("please message me the error you received")

def deserializer():
    with open(r'example.yml') as file:
        user = yaml.full_load(file)
    return user

if __name__ == "__main__":
    user = deserializer()
    helper=auto.Driver(user["path"])  
    if(helper.signIn(user["email"],user["pwd"])):
        if(helper.joinMeeting()):
            time.sleep(1200)
            helper.endMeeting()
            #between class
            time.sleep(960)
            helper.joinMeeting()
            time.sleep(3600)
            helper.endMeeting()            
        else:
            err()

    else:
        err()
    