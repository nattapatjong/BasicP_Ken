# sum = 0
# n = 3

# for i in range(n):
#     sum += i+1

# print(sum)


# for i in range(10):
#     if (i % 2) == 0:
#         print("Even number: ",i)

# sum = int(input("Enter your number: "))
# for i in range(12):
#     i += 1
#     x = sum*i
#     print(sum,"*",i,":",x)

# i = 0
# while i < 5:
#     print("hello")
#     i += 1
#     if i == 4:
#         break

start = True
while start:
    print("เลือกข้อที่ต้องการเล่น")
    print("ข้อที่ [1] โจทย์แรก")
    print("ข้อที่ [2] โจทย์แรก")
    x = int(input("กรุณากรอกเลข: "))
    if (x == 1):
        print("ทำโจทย์ที่ 1")
    elif (x == 2): 
        print("ทำโจทย์ที่ 2")
    start = False