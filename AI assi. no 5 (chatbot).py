""" Assignment No – 05 (Group B) Program to an elementary catboat for Simple
Question and Answering Application """
print("Simple Question and Answering Program")
print("=====================================")
print(" You may ask any one of these questions")
print("Hi")
print("How are you?")
print("Are you working?")
print("What is your name?")
print("what did you do yesterday?")
print("Quit")
while True:
    question = input("Enter one question from above list:")
    question = question.lower()
    if question in ['hi']:
         print("Hello")
    elif question in ['how are you?','how do you do?']:
         print("I am fine")
    elif question in ['are you working?','are you doing any job?']:
         print("yes. I'am working in KLU")
    elif question in ['what is your name?']:
         print("My name is Emilia")
         name=input("Enter your name?")
         print("Nice name and Nice meeting you",name)
    elif question in ['what did you do yesterday?']:
         print("I  went for swmimmng")
    elif question in ['quit']:
         break
    else:
         print("I don't understand what you said")