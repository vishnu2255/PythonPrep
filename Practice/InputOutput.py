userdata = input("Enter a num \n")
print(userdata)

while True:
    try:
        useda = input("Enter a num")
        num = int(useda)
    except ValueError:
        print("Enter a valid number")
    else:
        print(num)
        break

