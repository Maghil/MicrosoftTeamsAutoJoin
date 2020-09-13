import auto
import yaml
import time

def err():                                    #to print instruction if error arises
    print("please message me the error you received")

def deserializer():                            #deserializes yml file
    with open(r'welcome.yml') as file:
        user = yaml.full_load(file)
    return user

def cur_time():                                #used to get current system time
    localtime = time.localtime(time.time())
    cur_time=int(str(localtime.tm_hour)+str(localtime.tm_min).zfill(2))
    return(cur_time)


def wait_till(start_time):                      #used to wait till the time matches
    if(cur_time() == start_time or cur_time() > start_time):
        pass
    else:
        print("waiting for :"+str(start_time))
        time.sleep(15)
        wait_till(start_time)
    return(True)



if __name__ == "__main__":
    user = deserializer()
    helper=auto.Driver()

    if(helper.signIn(user["email"],user["pwd"])):   #going through all assigned meetings 
        classes = user["classes"]   
        for i in classes.items():
            a=i[1]
            start_time=a["startTime"]
            end_time=a["endTime"]
            print(cur_time())
            print(end_time)
            if(cur_time()>end_time):                #if the meeting end time lapsed no point joining
                print("missed meeting")               
            
            elif(wait_till(start_time)):            #if the program start running before start time it waits 
                print("joining meeting")
                if helper.joinMeeting():            
                    if(wait_till(end_time)):        #waits for end time then ends meeting
                        helper.endMeeting()
                    else:
                        print("cant find end button")
                else:
                    err()
    else:
        err()
    