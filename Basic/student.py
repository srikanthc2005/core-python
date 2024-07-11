marks = []
total = 0
average = 0

def set_marks():
    print("Enter 6 subject marks: ")
    for i in range(6):
        marks.append(int(input(f"Enter subject {i+1}'s marks: ")))
    print("Marks saved in list")

def get_total():
    global total
    total = sum(marks)
    print(f"Total marks = {total}")

def get_avg():
    global average
    average = total/6
    print(f"Average marks = {average}")

def is_passed():
    global marks
    i = 0
    while i<6:
        if marks[i] > 33:
            break
    if i == len(marks):
        print("Pass")
    else:
        print("Fail")

def disp_marks():
    global marks
    for i in range(6):
        print(marks[i])
    
    
