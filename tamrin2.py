hoghogh=int(input("hoghogh:"))

if hoghogh>100:
    hoghogh_1=hoghogh-(hoghogh*0.35)
    print(hoghogh_1)

if 80<=hoghogh<=100:
    hoghogh_2=hoghogh-(hoghogh*0.25)
    print(hoghogh_2)

if 70<=hoghogh<80:
    hoghogh_3=hoghogh-(hoghogh*0.15)
    print(hoghogh_3)

if 60<=hoghogh<70:
    hoghogh_4=hoghogh-(hoghogh*0.12)
    print(hoghogh_4)

if 50<=hoghogh<60:
    hoghogh_5=hoghogh-(hoghogh*0.10)
    print(hoghogh_5)

if 40<=hoghogh<50:
    hoghogh_6=hoghogh-(hoghogh*0.05)
    print(hoghogh_6)

if hoghogh<40:
    hoghogh_7=hoghogh
    print(hoghogh_7)