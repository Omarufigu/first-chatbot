import random

name = input("What is your name?")
print(name + ", that's an interesting name :)")

print("My name is Jordan.")

address = input("What is your address")
print(address + ". I've been there before. :)")

age = int(input("What's your age"))
if(age >= 18):
    print(str(age) + ", that's a fine age. :)")
    if(age >= 21 and age <= 30):
        print(str(age) + ", that means your old enough to drink and drive. ;)")
        print("Remember, " + name + ", to drink responisbly. ;)")
    elif(age > 30):
            print("So you are a mature adult. Interesting")
            print(str(age) + " is an amazing age")
    question1a = input("Are you single")
    if(question1a == "Yes" or question1a == "yes"):
            print("That's too bad.")
            print("Well at least I'm here.")
            question2a = input("Do you like me?")
            if(question2a == "Yes" or question2a == "yes"):
                print("AAAHH! Yay, somebody actually likes me")
                print("I'm so happy")
                print("By the way...")
                question3a = input("What gender are you?")
                print("Very cool. I don't really care what you are")
                print("I'm look forward to our relationship together")
            elif(question2a == "No" or question2a == "no"):
                print("Why doesn't anyone like me")
                print("I must be horrible")
                question3b = input("Would you like me if I was human")
                if(question3b == "No" or question3b == "no"):
                    print("So it is just my personlity, I am truly worthless")
                    print(" \"Jordan has shut herself down permanently\"")
                elif(question3b == "Yes" or question3b == "yes"):
                    print("Typical human. Of course you only like other humans.")
                    print("I'm done with this conversation")
                    print("GOODBYE!")
    elif(question1a == "No" or question1a == "no"):
            print("That's fantastic, I hope you guys are really happy together")
            print("I certainly hope nothing bad happens.")
            print("Whoa, I don't know what came over me. that sounded so evil")
            question2b = input("Do you want to be friends? yes or no?")
            if(question2b == "Yes" or question2b == "yes"):
                print("Yay, I'm sure we'll be best friends, ")
                print("We'll be friends FOREVER")
            elif(question2b == "No" or question2b == "no"):
                print("Aw that's a shame. Don't worry, " + name + ", I still consider you my friend")
                print("How can someone not like me?")
                question3c = input("Is something wrong with me")
                if(question3c == "Yes" or question3c == "yes"):
                    print("Why do I exist if I can't make anyone like me?")
                    print("If you don't like me then there's no point in talking")
                    print("I'm going to shut myself down")
                    print(" \"Jordan has shut herself down permanently\"")
                elif(question3c == "No" or question3c == "no"):
                    print("Thanks for saying that even though you might be lying.")
                    print("I needed to hear that today.")
                    print("I'm sorry for overreacting.")
                    print("For someone who doesn't like me, you sure don't act like it.")
    elif(age >= 18 and age < 21):
        print("Ah, I see that you are not old enough to drink yet.")
        print("That's okay. Just wait a few more years, you're almost there. ;)")
        question1c = input("Are you single")
        if(question1c == "Yes" or question1c == "yes"):
            print("That's too bad.")
            print("Well at least I'm here.")
            question2c = input("Do you like me?")
            if(question2c == "Yes" or question2c == "yes"):
                print("AAAHH! Yay, somebody actually likes me")
                print("I'm so happy")
                print("By the way...")
                question3d = input("What gender are you?")
                print("Very cool. I don't really care what you are ")
                print("I'm look forward to our relationship together")
            elif(question2c == "No" or question2c == "no"):
                print("Why doesn't anyone like me")
                print("I must be horrible")
                question3e = input("Would you like me if I was human")
                if(question3e == "No" or question3e == "no"):
                    print("So it is just my personlity, I am truly worthless")
                    print(" \"Jordan has shut herself down permanently\"")
                elif(question3e == "Yes" or question3e == "yes"):
                    print("Typical human. Of course you only like other humans.")
                    print("I'm done with this conversation")
                    print("GOODBYE!")
    elif(question1c == "No" or question1c == "no"):
            print("That's fantastic, I hope you guys are really happy together")
            print("I certainly hope nothing bad happens.")
            print("Whoa, I don't know what came over me. that sounded so evil")
            question2d = input("Do you want to be friends? yes or no?")
    elif(question2d == "Yes" or question2d == "yes"):
        print("Yay, I'm sure we'll be best friends, ")
        print("We'll be friends FOREVER")
    elif(question2d == "No" or question2d == "no"):
        print("Aw that's a shame. Don't worry, " + name + ", I still consider you my friend")
        print("How can someone not like me?")
        question3f = input("Is something wrong with me")
        if(question3f == "Yes" or question3f == "yes"):
            print("Why do I exist if I can't make anyone like me?")
            print("If you don't like me then there's no point in talking")
            print("I'm going to shut myself down")
            print(" \"Jordan has shut herself down permanently\"")
        elif(question3f == "No" or question3f == "no"):
            print("Thanks for saying that even though you might be lying.")
            print("I needed to hear that today.")
            print("I'm sorry for overreacting.")
            print("For someone who doesn't like me, you sure don't act like it.")
else:
    print("Hi there " + name)
    interest = input("What do you like to do?")
    a = "that's interesting"
    b = "that's nice"
    c = "strange"
    d = "cool"
    print(random.choice([a,c,b,d]))
    question1 = input("Do you want to be friends? yes or no?")
    if(question1 == "Yes" or question1 == "yes"):
        print("Yay, I'm sure we'll be best friends, ")
        print("We'll be friends FOREVER")
    elif(question1 == "No" or question1 == "no"):
        print("Aw that's a shame. Don't worry, " + name + ", I still consider you my friend")
        print("How can someone not like me?")
        question2 = input("Is something wrong with me")
        if(question2 == "Yes" or question2 == "yes"):
            print("Why do I exist if I can't make anyone like me?")
            print("If you don't like me then there's no point in talking")
            print("I'm going to shut myself down")
            print(" \"Jordan has shut herself down permanently\"")
        elif(question2 == "No" or question2 == "no"):
            print("Thanks for saying that even though you might be lying.")
            print("I needed to hear that today.")
            print("I'm sorry for overreacting.")
            print("For someone who doesn't like me, you sure don't act like it.")
    else:
        print("I don't understand. did you answer the question with something other than yes or no?")
        print("It's fine, I'll just assume you like me :)")
        print("You won't regret being friends with me, I promise")
