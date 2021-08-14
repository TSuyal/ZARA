from pygame import mixer
import datetime
import time
import pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def gettime():
    return datetime.datetime.now()

def Wish_me():
    hour=int(datetime.datetime.now().hour)
    if(hour==0 and hour<=12):
        speak("good morning")
    elif(hour>=12 and hour<18):
        speak("good afternoon")
    else:
        speak("good evening")
    day=datetime.datetime.now().day
    month=datetime.datetime.now().month
    year=datetime.datetime.now().year
    date=datetime.datetime.now().date
    speak("Hello my name is zara guyss")
    speak("Today is")
    speak(day)
    if month==1:
        speak("january")
    elif month==2:
        speak("February")
    elif month==3:
        speak("march")
    elif month==4:
        speak("April")
    elif month==5:
        speak("may")
    elif month==6:
        speak("june")
    elif month==7:
        speak("july")
    elif month==8:
        speak("august")
    elif month==9:
        speak("september")
    elif month==10:
        speak("october")
    elif month==11:
        speak("november")
    else:
        speak("December")
    speak(year)
    

def music(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        x=int(input())
        if x==stopper:
            mixer.music.stop()
            break

def create(k):
    with open(k,"x") as ptr:
        print("Create sucessfully......")

def log(l):
    value=input("log the data:")
    with open(l,"a") as ptr:
        ptr.write(str([str(gettime())]) +":"+value+"\n")
        print("Written sucessfully.....")

def retrieve(r):
    with open(r) as ptr:
        rd=ptr.read()
        print(rd)

def q1():
    with open("E:\\ZARA\\ques_1.txt")as ptr:
        r=ptr.read()
        print(r)

def q2():
    with open("E:\\ZARA\\ques_2.txt") as ptr:
        r=ptr.read()
        print(r)

def q3():
    with open("E:\\ZARA\\ques_3.txt") as ptr:
        r=ptr.read()
        print(r)

def q4():
    with open("E:\\ZARA\\ques_4.txt") as ptr:
        r=ptr.read()
        print(r)

def q5():
    with open("E:\\ZARA\\ques_5.txt")as ptr:
        r=ptr.read()
        print(r)

def q6():
    with open("E:\\ZARA\\ques_6.txt")as ptr:
        r=ptr.read()
        print(r)

def q7():
    with open("E:\\ZARA\\ques_7.txt")as ptr:
        r=ptr.read()
        print(r)
def q8():
    with open("E:\\ZARA\\ques_8.txt")as ptr:
        r=ptr.read()
        print(r)

def q9():
    with open("E:\\ZARA\\ques_9.txt")as ptr:
        r=ptr.read()
        print(r)

def q10():
    with open("E:\\ZARA\\ques_10.txt")as ptr:
        r=ptr.read()
        print(r)


if __name__ == "__main__":
    Wish_me()
    speak("What do you want to do Tanya")
    speak("Do you want to play a game or you want to go to account system")
    speak("For game press 1")
    print("For game press 1")
    speak("For account system press 2")
    print("For account system press 2")
    x=int(input("Enter:"))
    if(x==1):
        speak("let's play")
        print("let's play")
        music("E:\\ZARA\\kbc.mp3",0)
        time.sleep(1)
        speak("This is your first level")
        speak("And you will have two questions in this level ")
        print("This is your first level")
        speak("Your first question is on your screen")
        print("Your first question is on your screen")
        q1()
        x=int(input("Enter your choice"))
        if(x==1):
            speak("Correct answer")
            print("Correct answer")
            music("E:\\ZARA\\Applause-a70ac5da-5e5d-3ea9-979e-69d993346abb.mp3",0)
            time.sleep(1)
            speak("Your second question is on your screen")
            print("Your second question is on your screen")
            q2()
            x=int(input("Enter your choice"))
            if(x==3):
                speak("correct answer")
                print("Correct Answer")
                speak("Congratulations you have passed your first level")
                print("Congratulations you have passed your first level")
                music("E:\\ZARA\\Applause-a70ac5da-5e5d-3ea9-979e-69d993346abb.mp3",0)
                time.sleep(1)
                speak("This is your second level")
                speak("And you will have four questions in this level")
                print("This is your second level")

                speak("Your first question is on your screen")
                print("Your first question is on your screen")
                q3()
                x=int(input("Enter your choice"))
                if x==3:
                    speak("Correct answer")
                    print("Correct answer")
                    music("E:\\ZARA\\Applause-a70ac5da-5e5d-3ea9-979e-69d993346abb.mp3",0)
                    time.sleep(1)
                    speak("second question is on your screen")
                    print("second question is on your screen")
                    q4()
                    x=int(input("Enter your choice"))
                    if x==3:
                        speak("Correct answer")
                        print("Correct answer")
                        music("E:\\ZARA\\Applause-a70ac5da-5e5d-3ea9-979e-69d993346abb.mp3",0)
                        time.sleep(1)
                        speak("third question is on your screen")
                        print("third question is on your screen")
                        q5()
                        x=int(input("Enter your choice"))
                        if x==3:
                            speak("Correct answer")
                            print("Correct answer")
                            music("E:\\ZARA\\Applause-a70ac5da-5e5d-3ea9-979e-69d993346abb.mp3",0)
                            time.sleep(1)
                            speak("fourth question is on your screen")
                            print("fourth question is on your screen")
                            q6()
                            x=int(input("Enter your choice"))
                            if x==2:
                                speak("Correct answer")
                                print("Correct answer")
                                speak("Congratulations you have passed your second level")
                                print("Congratulations you have passed your second level ")
                                music("E:\\ZARA\\Applause-a70ac5da-5e5d-3ea9-979e-69d993346abb.mp3",0)
                                time.sleep(1)
                                speak("This is your third level")
                                speak("And you have four questions in this level")
                                print("This is your third level")
                                speak("first question is on your screen")
                                print("first question is on your screen")
                                q7()
                                x=int(input("Enter your choice"))
                                if x==1:
                                    speak("Correct answer")
                                    print("Correct answer")
                                    music("E:\\ZARA\\Applause-a70ac5da-5e5d-3ea9-979e-69d993346abb.mp3",0)
                                    time.sleep(1)
                                    speak("second question is on your screen")
                                    print("second question is on your screen")
                                    q8()
                                    x=int(input("Enter your choice"))
                                    if x==4:
                                        speak("Correct answer")
                                        print("Correct answer")
                                        music("E:\\ZARA\\Applause-a70ac5da-5e5d-3ea9-979e-69d993346abb.mp3",0)
                                        time.sleep(1)
                                        speak("third question is on your screen")
                                        print("third question is on your screen")
                                        q9()
                                        x=int(input("Enter your choice"))
                                        if x==2:
                                            speak("Correct answer")
                                            print("Correct answer")
                                            music("E:\\ZARA\\Applause-a70ac5da-5e5d-3ea9-979e-69d993346abb.mp3",0)
                                            time.sleep(1)
                                            speak("fourth questtion is on your screen")
                                            print("fourth questtion is on your screen")
                                            q10()
                                            x=int(input("Enter your choice"))
                                            if x==2:
                                                speak("Correct answer")
                                                print("Correct answer")
                                                speak("congratulations")
                                                speak(" you won the game")
                                                print("you won")
                                                music("E:\\ZARA\\kbc.mp3",0)
                                                time.sleep(1)
                                            else:
                                               # music("E:\\AUD-20191112-WA0019.mp4",0)
                                                speak("ooops game over")
                                                print("you lost")
                                        else:
                                            #music("E:\\AUD-20191112-WA0019.mp3",0)
                                            speak("ooops game over")
                                            print("You lost")
                                    else:
                                        #music("E:\\AUD-20191112-WA0019.mp3",0)
                                        speak("ooops game over")
                                        print("You lost")
                                else:
                                    #music("E:\\AUD-20191112-WA0019.mp3",0)
                                    speak("ooops game over")
                                    print("You lost")
                            else:
                                #music("E:\\AUD-20191112-WA0019.mp3",0)
                                speak("ooops game over")
                                print("You lost")
                        else:
                            #music("E:\\AUD-20191112-WA0019.mp3",0)
                            speak("ooops game over")
                            print("You lost")
                    else:
                        #music("E:\\AUD-20191112-WA0019.mp3",0)
                        speak("ooops game over")
                        print("Your lost")
                else:
                    # music("E:\\AUD-20191112-WA0019.mp3",0)
                    speak("ooops game over")
                    print("You lost")
            else:
                #music("E:\\AUD-20191112-WA0019.mp3",0)
                speak("ooops game over")
                print("You lost")
        else:
            #music("E:\\AUD-20191112-WA0019.mp4",0)
            speak("ooops game over")
            print("oops you lost")
    elif(x==2):    
        speak("Welcome in account system")
        speak("press one for create a student file ")
        speak("press two for log")
        speak("press 3 for retrieve")
        while(1):
            
            a=int(input("press 1 for create a student file:\npress 2 for log:\npress 3 for retrieve \n"))
            try:
                if a==1:
                    speak("Create a file with path")
                    b=input("Create a file with path:")
                    create(b)
                elif a==2:    
                    speak("Enter the file name where ou want to log data")
                    c=input("Enter the file name where you want to log data:")
                    log(c)
                elif a==3:
                    speak("Enter the file name whose data you want to retrieve")
                    d=input("Enter the file name whose data you want to retrieve:")
                    retrieve(d)
                else:
                    speak("please press valid number")

                speak("Do you want to continue if yes press 1 otherwise press 0")
                print("Do you want to continue (0,1):")
                b=int(input())
                
                if (b==0):
                    break
            except Exception as e:
                speak(e)
                print(e)
       


        