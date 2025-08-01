marks = []

def add_marks():
    new_marks = int(input("Enter your marks :"))
    marks.append(new_marks)


def total_marks():
    add = sum(marks)
    avg = add / len(marks)
    print(f"total marks: {add}")
    print(f"average marks: {avg}")


def show_grade():
    avg = sum(marks) / len(marks)
    if avg >80 :
        print("Grade A")
    elif avg >50 :
        print("Grade B")
    elif avg <= 50:
        print("Grade C")
    else :
        print("Grade E")

while True:
    print("=====Marks Manager=====")
    print("1. Add subject marks")
    print("2. Show total and Average")
    print("3. Show Grade")
    print("4.Exit")
    
    choice = input("Enter your choice : ")
     
    if choice == "1":
        add_marks()
    elif choice == "2":
        total_marks()
    elif choice == "3":
        show_grade()
    elif choice == "4":
        print("Exiting.....bye!!")
        break 
    else :
        print("Something invaled choice....")