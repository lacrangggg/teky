
# some variables and contants
student_list = []

def view_my_list():
    if student_list:
        print(f"{"Name":<30}\t{"Age":<5}\t{"Maths":<5}\t{"Literature":<10}\t{"English":<7}\t{"Avg. Grade":^15}\t{"Ranked":^10}")
        print("_"*100)
        for i in student_list:

            
            print(f"{i["name"]:<30} \t {i["age"]:<5} \t {i["maths_grade"]:<5} \t {i["literature_grade"]:<10} \t {i["english_grade"]:<7} \t {i["avg"]:<3.2f} \t {i["rank"]:<3}")
    else:
        print("There are no students here!")
    return main() #back to the menu

def get_valid_grade(prompt):
    while True:
        try:
            grade = float(input(prompt)) 
            if 0 <= grade <= 10:
                return grade
            else:
                print("Invalid grade! Please enter a number between 0 and 10.")
        except ValueError:
               print("Invalid input! Please enter a valid number.")

def add_new_item():
    name = input("Student's name: ")
    age = input("Student's age: ")
    maths_grade = get_valid_grade("Student's maths grade: ")
    literature_grade = get_valid_grade("Student's literature grade: ")
    english_grade = get_valid_grade("Student's english grade: ")

    avg_grade = (maths_grade + literature_grade + english_grade)/3
    if 0<= avg_grade < 5.0: ranked = "Weak"
    elif 5.0 <= avg_grade < 6.5: ranked = "Average"
    elif 6.5 <= avg_grade < 8.0: ranked = "Good"
    elif 8.0 <= avg_grade <=10: ranked = "Excellent"

    student_list.append( {"name" : name, "age": age, "maths_grade": maths_grade, "literature_grade": literature_grade, "english_grade": english_grade, "avg": avg_grade, "rank":ranked})
    print("Successfully added new student!")
    return main()

def find_item():
    name = input("Enter the name which you want to find: ")
    name = name.lower() #se dua string vua nhap thanh cac ky tu viet thuong
    print(f"{"Name":<30}\t{"Age":<5}\t{"Maths":<5}\t{"Literature":<10}\t{"English":<7}\t{"Avg. Grade":^15}\t{"Ranked":^10}")
    print("_"*100)
    
    for i in student_list:
        if i["name"].lower() == name:
            
            print(f"{i["name"]:<30} \t {i["age"]:<5} \t {i["maths_grade"]:<5} \t {i["literature_grade"]:<10} \t {i["english_grade"]:<7} \t {i["avg"]:<3.2f} \t {i["rank"]:<3}")


    return main()

def remove_item():
    if student_list:
        print(f"{"Index":<5}\t{"Name":<30}\t{"Age":<5}\t{"Maths":<5}\t{"Literature":<10}\t{"English":<7}\t{"Avg. Grade":^15}\t{"Ranked":^10}")
        print("_"*100)
        
        for i in range(len(student_list)):
            print(f"{i+1:<5} {student_list[i]["name"]:<30} \t {student_list[i]["age"]:<5} \t {student_list[i]["maths_grade"]:<5} \t {student_list[i]["literature_grade"]:<10} \t {student_list[i]["english_grade"]:<7} \t {student_list[i]["avg"]:<3.2f} \t {student_list[i]["rank"]:<3}")
        r = int(input("Remove student: "))
        while 1<=r<=len(student_list):
            student_list.pop(r-1)
            print("Item removed successfully!")
            return main()
    else:
        print("There are no students here!")
        return main()

def main():
    print('''
    1. View my list
    2. Find by name
    3. Add new items
    4. Remove items
    Q. Quit
    ''')

    opts = ['1','2','3','4','Q'] #If user did not input these char so the program will break
    user_input = input("Choose your option: ") #input a STRING
    user_input = user_input.upper() #E or e, Q or q are the same things
    
    if user_input not in opts:
        print("It is not a correct option, try again")
        return main() #recursion, give user a chance to try again 

    if user_input == '1': print(view_my_list())
    if user_input == '2': print(find_item())
    if user_input == '3': print(add_new_item())
    if user_input == "4": print(remove_item())
    if user_input == 'Q': exit()


if __name__ == '__main__':
    main()