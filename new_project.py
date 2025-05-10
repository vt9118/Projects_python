timestamp = input("Enter the current time:")

# import time
# timestamp=time.strftime('%H:%M:%S')
if(timestamp<'12:00:00'):
    print("Good morning")
elif(timestamp>'12:00:00'):
    print("Good afternoon")

