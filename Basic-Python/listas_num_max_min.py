print("Calculating Maximums and Minimums")


fin = list()
while True:
    try:
        num = input("Enter some numbers : ")
        if num == "hecho":
             print("done")
             print(fin)
             print(max(fin))
             print(min(fin))
             break
        else:
            pre = float(num)
            fin.append(pre)
            #print(num)
    except:
        print("Enter a valid number")

print("That´s it")
