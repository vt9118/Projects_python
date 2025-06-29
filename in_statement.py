# give_error = ("subscribe ")
# give_error2 = "like" 
# give_error3 = "comment"
# give_error4 = "buy this product"

# message = input("Enter the message: ")
# if((give_error in message ) or ( give_error2 in message) or (give_error3 in message) or (give_error4 in message)):
#     print("This message is in spam")

# else: 
#     print("This message is not in spam")

#Project to check your name in the list or not
Names = ["Vishal", "Badal", "Chandan", "Aman", "Ankit"]

i = (input("Enter your name: ").capitalize())
if i in Names :
    print("Your name is in the list")
else :
    print("Your name is not in the list")