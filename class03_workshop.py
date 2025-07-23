ท่านชัชชาติ = 1000000
ไม้จิ้มฟัน = 2
dual_sword = 499
RPG = 9999

start = True

while start:
    print("ยินดีต้อนรับสู่ดันเจี้ยนลับของเรา")
    print("จะต่อสู้ หรือ จะหนีจงเลือกมา: ")
    print("ทางที่ [1] ต่อสู้")
    print("ทางที่ [2] หนี")
    x = int(input("กรุณาเลือกเส้นทางของคุณ: "))
    if (x == 1):
        attack_times = int(input("อยากจะตีกี่ที: "))
        for i in range(attack_times):
            print("เจ้าคิดผิดแล้วที่เลือกจะสู้ เจ้าไม่มีทางหนีไปจากที่นี่ได้หรอก")
            print("--------Choose-your-weapon-to-attack--------")
            print("อาวุธ [1] ไม้จิ้มฟัน: ",ไม้จิ้มฟัน)
            print("อาวุธ [2] Dual sword: ",dual_sword)
            print("อาวุธ [3] RPG: ",RPG)
            print("เหลือเลือด: ",ท่านชัชชาติ)
            print("เหลือโอกาศตีอยู่:",attack_times - i)
            weapon = int(input("เลือกอาวุธที่จะใช้ตี: "))
            print("คุณเลือกอาวุธ",weapon)
            if (weapon == 1):
                ท่านชัชชาติ -= ไม้จิ้มฟัน
                print("Monster health",ท่านชัชชาติ)
            if (weapon == 2):
                ท่านชัชชาติ -= dual_sword
                print("Monster health",ท่านชัชชาติ)
            if (weapon == 3):
                ท่านชัชชาติ -= RPG
                print("Monster health",ท่านชัชชาติ)
        start = False
    else:
        print("อ่อน หนีทำไมเป็นพระเอกไม่ใช่ออ")
        break
