ghad=float(input("ghad:"))
vazn=float(input("vazn:"))

bmi=vazn/(ghad**2)
print("bmi:",bmi)

if bmi<18.5:
    print("kambood vazn")

if 18.5<=bmi<25:
    print("vazn monaseb")

if 25<=bmi<30:
    print("ezafe vazn")

if bmi>=30:
    print("chaghi")