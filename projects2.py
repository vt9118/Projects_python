print("Let's play KBC:")

question =("1. What is the capital of India?")
options = ("A. Delhi", "B. Mumbai", "C. Kolkata", "D. Chennai")

print(question)
print(options)
answer1 = input("Enter your answer : ").strip().upper()

if answer1 =="A":
    print("Correct!")
else:
    print("Wrong answer!")

question1 = ("2. What is the capital of India?")
options2 = ("A. Delhi ","B. Mumbai ","C.Kolkata ","D. Chennai")

print(question1)
print(options2)

answer2 = input("Enter your answer : ").strip().upper()

if answer2 =="A":
    print("Correct!")
else:
    print("Wrong answer!")


question3 = ("3. Who is known as the Father of the Nation in India?")
options3 = ("A. Jawaharlal Nehru ", "B . Mahatma Gandhi ", "C. Subhash Chandra Bose ", "D. Bhagat Singh")

print(question3)
print(options3)

answer3 = input("Enter your answer : ").strip().upper()

if answer3 =="B":
    print("Correct!")
else:
    print("Wrong answer!")


question4 = ("4. Whar is the National Animal fo India ?")
options4 = ("A. Lion ", "B. Tiger ", "C. Elephant ", "D. Peacock")

print(question4)
print(options4)

answer4 = input ("Enter your answer : ").strip().upper()

if answer4 =="D":
    print("Correct!")
else:
    print("Wrong answer!")


# Check if all answers are correct
if answer1 == "A" and answer2 == "A" and answer3 == "B" and answer4 == "D":
    print("Congratulations! You have won the game!")
else:
    print("Better luck next time!")
