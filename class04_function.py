# def hello(x):
#     print(x)

# x = input()
# hello(x)

# def sum(a,b):
#     result = a + b
#     return result

# num1 = int(input("กรอกเลข1: "))
# num2 = int(input("กรอกเลข2: "))

# result = sum(num1,num2)
# sum(num1,num2)

def add(num1,num2):
    result = num1 + num2 
    return result

def minus(num1,num2):
    result = num1 - num2
    return result

def mutiple(num1,num2):
    result = num1 * num2
    return result

def divide(num1,num2):
    result = num1 / num2
    return result

def is_even(result):
    if result % 2 == 0:
        print("เลขคู่")
    else:
        print("เลขคี่")

def main():
    num1 = int(input("กรอกเลขตัวที่ 1: "))
    num2 = int(input("กรอกเลขตัวที่ 2: "))
    print(" + - * / เอาอันไหน")
    print("[1] +")
    print("[2] -")
    print("[3] *")
    print("[4] /")
    operation = input("เลือกสักอัน: ")
    if (operation == "1"):
        result = add(num1,num2)
        print("ผลบวกคือ:",result)
    elif (operation == "2"):
        result = minus(num1,num2)
        print("ผลลบคือ:",result)
    elif (operation == "3"):
        result = mutiple(num1,num2)
        print("ผลคูณคือ:",result)
    elif (operation == "4"):
        result = divide(num1,num2)
        print("ผลหารคือ:",result)
    
    is_even(result)

main()