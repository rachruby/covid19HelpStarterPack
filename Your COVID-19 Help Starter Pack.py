# Title: Your COVID-19 Starter Pack
# Description: This program informs the users about COVID-19 status, alarms the users to follow the safety measures, suggests the users whether or not they should get tested, and recommends the different age-groups into sectors about lifestyles and things to do during the quarantine. 
# Author: Rachel Zhang 
# Date: Jan. 15 2021


import sys, time, os

def typewriter(x):
    for char in x:
        sys.stdout.write(char)
        sys.stdout.flush()
        if char != "\n":
            time.sleep(0.02)
        else:
            time.sleep(1)
os.system("cls")

# Introduction (information about COVID-19 & safety measures) 
opening = "Hi there, this is Bot Rach, I am a bot that assist humans with \nthe update of COVID-19, safety measures, suggestion on COVID-19 tests, \nand Recommendation on things to do during quarantine, which basically mean that \nI am Your COVID-19 Starter Pack, so get ready with me!"   
typewriter(opening)
time.sleep(3)
print()
print("Before we begin, maximize your screen can result in better display quality!")
time.sleep(1)
print()
inform_COVID = "Coronavirus disease (COVID-19) is an infectious disease caused by a newly \ndiscovered coronavirus. People infected with the COVID-19 virus will experience \nmild to moderate respiratory illness and recover without requiring special treatment. Older people, and those with underlying medical problems like cardiovascular \ndisease, diabetes, chronic respiratory disease, and cancer are more likely to \ndevelop serious illness."
typewriter(inform_COVID)
time.sleep(3)
print()

safety_COVID = "That means it is really important to protect yourself and others by doing the \nfollowing steps provided by Bot Rach."
typewriter(safety_COVID)
time.sleep(3)
print()
print("Maintain at least a 1-metre distance between yourself and others to reduce your risk of infection when they cough, sneeze or speak.")
print()
time.sleep(3)
print("Make wearing a mask a normal part of being around other people. \nThe appropriate use, storage and cleaning or disposal are essential to make masks as effective as possible.")
print()
time.sleep(3)
print("Clean your hands before you put your mask on, as well as before and after you take it off, and after you touch it at any time.")
print()
time.sleep(3)
print("Regularly and thoroughly clean your hands with an alcohol-based hand rub or wash them with soap and water. \nThis eliminates germs including viruses that may be on your hands.")
print()
time.sleep(3)
print("Avoid touching your eyes, nose and mouth.")
print()
time.sleep(3)
print("Cover your mouth and nose with your bent elbow or tissue when you cough or sneeze.")
print()
time.sleep(3)
print("Clean and disinfect surfaces frequently especially those which are regularly touched, \nsuch as door handles, faucets and phone screens.")
print()
time.sleep(3)

# COVID-19 Testing Quiz
testing_COVID = "Alright, as the job of a hospitable bot. I am going to lead you into a COVID-19 check-up to further assist you with your physical and mental well being."
print("Please enter (Y/N) for below questions")
question_1 = input("Have you recently been out in a crowded area without the safety measures mentioned above?")
question_1.upper()

question_2 = input("Is there a recent COVID-19 outbreak in your area?")
question_2.upper()

question_3 = input("Do you have a fever, dry cough, tiredness, loss of taste or smell, aches and pains, headache, sore throat, nasal congestion, red eyes, diarrhoea, or a skin rash in the recent week?")
question_3.upper()

if question_1 == 'Y' and question_2 == 'Y' and question_3 == 'Y':
    print("You should definitely go get tested for COVID-19 in your local community")

elif question_1 == 'Y' and question_2 == 'Y':
    print("You should definitely go get tested for COVID-19 in your local community")

elif question_1 == 'Y' and question_3 == 'Y':
    print("You should definitely go get tested for COVID-19 in your local community")
else:
    print("You don't need a COVID-19 test")

# Recommendation Activities to do during quarantine
opening_recommendation = "Hopefully you had some useful assistance from me, ohhh, I almost forgot to introduce you to my recommendation on activities to do during quarantine"
typewriter(opening_recommendation)
time.sleep(2)
print("Do you want to some recommendations?")
recommendation_option = input("Enter (Y/N)")
recommendation_upper = recommendation_option.upper()

while recommendation_upper == "Y":
    username = input("Please enter your name: ")
    age = int(input("Please enter your age: "))
    if 0<age <= 17:
        option = int(input("Do you want to know recommendations on: Entertainment(1), Education(2), Mental Health(3): "))
        if option == 1:
            description = "There are some of the most popular Entertainment applications and games to share with you"
            typewriter(description)
            print()
            print("Youtube")
            time.sleep(2)
            print("A simple way for people to store videos online and share them with others. YouTube videos cover any topic anyone cares to upload a video about.")
            print()
            time.sleep(3)
            print("Youtube also allows users to watch videos online and communicate with people online")
            print()
            time.sleep(3)
            print("Youtube Kids")
            time.sleep(2)
            print("Youtube Kids offers educational videos and entertainment content to inspire and enhance young minds. It's one of the best learning apps for kids out there, as it offers them an easy way to watch their favorite shows.")
            print()
            time.sleep(3)
            print("[Note from Bot Rach: too much electronics is bad for your overall health] ")
            print()
            time.sleep(2)
            print("we, humans, can have fun not only with our technology, but also in the nature while social distancing, introduce you to EXERCISING")
            print()
            time.sleep(3)
            print("Grab a rope and jump in the undisturbed nature while social distancing")
            print()
            time.sleep(3)
            print("Or run in the nature and take the time to appreciate the nature and the animals during the pandemic")
            print()
            time.sleep(3)
            print("Last but not least, you can play board games with parents, or have online calls to your friends to play games virtually. ")
            print()
            time.sleep(3)
            closing = 'Hope you consider some of the recommendations on entertainment I made to do during quarantine. Hope you stay healthy and cozy during this pandemic, remember to apply the safety measures!'
            typewriter(closing)
            break
        elif option == 2:
            description = 'There are two of the most popular educational applications to share with you...'
            typewriter(description)
            print()
            print("Class Dojo")
            time.sleep(2)
            print("Educational application that allows primary school teachers, students and families through communication features, such as a feed for photos and videos from the school day, and messaging that can be translated into more than 35 languages.")
            print()
            time.sleep(3)
            print("Duolingo")
            time.sleep(2)
            print("A great application to learn foreign languages")
            print()
            print("Involves cool game practices and tests to further enhance the learning experience for users")
            print()
            time.sleep(3)
            closing = 'Hope you consider some of the recommendations on education I made to do during quarantine. Hope you stay healthy and cozy during this pandemic, remember to apply the safety measures!'
            typewriter(closing)
            break
        elif option == 3:
            description = 'There are many ways to cope with mental health, but first of all, you need to VALUE yourself! Treat yourself with kindness and respect, and avoid self-criticism.'
            typewriter(description)
            print()
            print("Make time for your hobbies and favorite projects, or broaden your horizons. Do a daily crossword puzzle, plant a garden, learn to play an instrument or become fluent in another language.")
            print()
            time.sleep(3)
            print("Take care of your body, meaning eat healthy, drink plenty of water, EXERCISE (go out in nature and enjoy the treasure mother earth provided to you), and get enough sleep (have a healthy sleeping schedule to reduce stress and burden).")
            print()
            time.sleep(3)
            print("I am sure these tips and tricks would help you cope with mental health, trust me, give ‘em a try! [wink wink]")
            print()
            time.sleep(2)
            print("For further information on coping with mental health and stress, you can always visit your local mental health helplines to reach out to get detailed support and assistance.")
            print()
            time.sleep(3)
            closing = 'Hope you consider some of the recommendations on coping with mental health I made to do during quarantine. Hope you stay healthy and cozy during this pandemic, remember to apply the safety measures!'
            typewriter(closing)
            break    
        else:
            print("Please choose a valid option.")
    elif age == 18 or 18<age<=30:
        option = int(input("Do you want to know recommendations on: Entertainment(1), Mental Health(2), Social Life(3): "))
        if option == 1:
            description = "There are some of the most popular Entertainment applications and games to share with you"
            typewriter(description)
            print()
            print("Youtube")
            time.sleep(2)
            print("A simple way for people to store videos online and share them with others. YouTube videos cover any topic anyone cares to upload a video about.")
            print()
            time.sleep(3)
            print("Youtube also allows users to watch videos online and communicate with people online")
            print()
            time.sleep(3)
            print("Tik Tok")
            time.sleep(2)
            print("The social media platform is used to make a variety of short-form videos, from genres like dance, comedy, and education, that have a duration from three seconds to one minute")
            print()
            time.sleep(3)
            print("Netflix")
            time.sleep(2)
            print("Netflix is a subscription-based streaming service that allows our members to watch TV shows and movies without commercials on an internet-connected device.")
            print()
            time.sleep(3)
            print("[Note from Bot Rach: too much electronics is bad for your overall health] ")
            print()
            time.sleep(3)
            print("we, humans, can have fun not only with our technology, but also in the nature while social distancing, introduce you to EXERCISING")
            print()
            time.sleep(3)
            print("Grab a rope and jump in the undisturbed nature while social distancing")
            print()
            time.sleep(3)
            print("Or run in the nature and take the time to appreciate the nature and the animals during the pandemic")
            print()
            time.sleep(2)
            print("Last but not least, you can play board games with your family members, or have online calls to your friends and family to play games virtually.")
            print()
            time.sleep(3)
            closing = 'Hope you consider some of the recommendations on entertainment I made to do during quarantine. Hope you stay healthy and cozy during this pandemic, remember to apply the safety measures!'
            typewriter(closing)
            break            
        elif option == 2:
            description = 'There are many ways to cope with mental health, but first of all, you need to VALUE yourself! Treat yourself with kindness and respect, and avoid self-criticism.'
            typewriter(description)
            print()
            time.sleep(2)
            print("Make time for your hobbies and favorite projects, or broaden your horizons. Do a daily crossword puzzle, plant a garden, learn to play an instrument or become fluent in another language.")
            print()
            time.sleep(3)
            print("Take care of your body, meaning eat healthy, drink plenty of water, EXERCISE (go out in nature and enjoy the treasure mother earth provided to you), and get enough sleep (have a healthy sleeping schedule to reduce stress and burden).")
            print()
            time.sleep(3)
            print("Lastly, avoid alcohol and smoking, sometimes people use alcohol and smoking  to 'self-medicate' but in reality, alcohol and smoking only aggravate problems.")
            print()
            time.sleep(3)
            print("For further information on coping with mental health and stress, you can always visit your local mental health helplines to reach out to get detailed support and assistance.")
            print()
            time.sleep(3)
            closing = 'Hope you consider some of the recommendations on coping with mental health I made to do during quarantine. Hope you stay healthy and cozy during this pandemic, remember to apply the safety measures!'
            typewriter(closing)
            break    
        elif option == 3:
            description = "Having a 'normal' social life is when the part of a person's time spent doing enjoyable things with others but with the global pandemic, everything is going to change a little. That is why I am here to introduce you to some of the software applications to enhance your social life during the outbreak."
            typewriter(description)
            print()
            time.sleep(2)
            print("Instagram")
            print("The social media platform allows users to share photos and videos, and even hosts live streaming capabilities. This application is the best way to communicate and socialize with friends virtually.")
            print()
            time.sleep(3)
            print("Facebook")
            print("Facebook allows users to connect with friends, family, and acquaintances across the globe. Similar to Instagram, this app allows users to communicate with friends and family more intimately.")
            print()
            time.sleep(3)
            print("Of course, connecting with friends and family is not the only way to be social, job-finding is also an important part of social life (p.s. Social networking)")
            print()
            time.sleep(2)
            print("LinkedIn")
            print("You can use LinkedIn to find the right job or internship, connect and strengthen professional relationships, and learn the skills you need to succeed in your career.")
            print()
            time.sleep(3)
            closing = 'Hope you consider some of the recommendations on social life I made for quarantine periods. Hope you stay healthy and cozy during this pandemic, remember to apply the safety measures!'
            typewriter(closing)
            break       
        else:
            print("Please choose a valid option.")

    elif age == 31 or 31<age<=100:
        option = int(input("Do you want to know recommendations on: Entertainment(1), Mental Health(2), Social Life(3): "))
        if option == 1:
            description = "There are some of the most popular Entertainment applications and games to share with you"
            typewriter(description)
            print()
            print("Youtube")
            time.sleep(2)
            print("A simple way for people to store videos online and share them with others. YouTube videos cover any topic anyone cares to upload a video about.")
            print()
            time.sleep(3)
            print("Youtube also allows users to watch videos online and communicate with people online")
            print()
            time.sleep(3)
            print("Netflix")
            time.sleep(2)
            print("Netflix is a subscription-based streaming service that allows our members to watch TV shows and movies without commercials on an internet-connected device.")
            print()
            time.sleep(3)
            print("[Note from Bot Rach: too much electronics is bad for your overall health] ")
            print()
            time.sleep(3)
            closing = 'Hope you consider some of the recommendations on entertainment I made to do during quarantine. Hope you stay healthy and cozy during this pandemic, remember to apply the safety measures!'
            typewriter(closing)
            break                        
        elif option == 2:
            description = 'There are many ways to cope with mental health, but first of all, you need to VALUE yourself! Treat yourself with kindness and respect, and avoid self-criticism.'
            typewriter(description)
            print()
            time.sleep(2)
            print("Make time for your hobbies and favorite projects, or broaden your horizons. Do a daily crossword puzzle, plant a garden, learn to play an instrument or become fluent in another language.")
            print()
            time.sleep(3)
            print("Surround yourself with positive, trustworthy people.")
            print()
            print("People with strong family or social connections are generally healthier than those who lack a support network.")
            print()
            time.sleep(3)
            print("Take care of your body, meaning eat healthy, drink plenty of water, EXERCISE (go out in nature and enjoy the treasure mother earth provided to you), and get enough sleep (have a healthy sleeping schedule to reduce stress and burden).")
            print()
            time.sleep(3)
            print("Lastly, avoid alcohol and smoking, sometimes people use alcohol and smoking  to 'self-medicate' but in reality, alcohol and smoking only aggravate problems.")
            print()
            time.sleep(3)
            print("For further information on coping with mental health and stress, you can always visit your local mental health helplines to reach out to get detailed support and assistance.")
            print()
            time.sleep(2)
            closing = 'Hope you consider some of the recommendations on coping with mental health I made to do during quarantine. Hope you stay healthy and cozy during this pandemic, remember to apply the safety measures!'
            typewriter(closing)
            break                
        elif option == 3:
            description = "Having a 'normal' social life is when the part of a person's time spent doing enjoyable things with others but with the global pandemic, everything is going to change a little. That is why I am here to introduce you to some of the software applications to enhance your social life during the outbreak."
            typewriter(description)
            print()
            time.sleep(2)
            print("Facebook")
            print("Facebook allows users to connect with friends, family, and acquaintances across the globe. Similar to Instagram, this app allows users to communicate with friends and family more intimately.")
            print()
            time.sleep(3)
            print("Of course, connecting with friends and family is not the only way to be social, job-finding is also an important part of social life (p.s. Social networking)")
            print()
            time.sleep(3)
            print("LinkedIn")
            print("You can use LinkedIn to find the right job or internship, connect and strengthen professional relationships, and learn the skills you need to succeed in your career.")
            print()
            time.sleep(3)
            closing = 'Hope you consider some of the recommendations on social life I made for quarantine periods. Hope you stay healthy and cozy during this pandemic, remember to apply the safety measures!'
            typewriter(closing)
            break                   
        else:
            print("Please choose a valid option.")
    else:
        print("Please enter a valid age")
while recommendation_upper == "N":
    print("Hope you stay healthy and cozy during this pandemic, remember to apply the safety measures!")
    break
