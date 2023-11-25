    a=6 * 9
def global_answer():
    a=6 * 7
    print("the value of a inside the fuction is",a)
    global_answer()
    print("the value of a outside the function is",a)
