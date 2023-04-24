# This is my first program

name = "Victor"
interest1 = "programming"
interest2 = "piano"
interest3 = "electronic music"

answer = input("""Hello and welcome to my first project!
Would you like me to introduce myself?

Answer yes or no: """)

if answer == "yes":
    print(f"""
My name is {name} and I'm an aspiring software developer. 
Right now I'm learning Python basics and trying to understand GitHub. 
My interests besides {interest1}, is playing the {interest2} and listening to {interest3}.
""")

    answer_2= input("Wanna help a beginner? yes/no: ")

    if answer_2 == "yes":
        print("""
Give me some tips and tricks that proved helpful to you!
Drop it in my DM. Cheers!
""")


else:
    print("Well, then I won't.")

