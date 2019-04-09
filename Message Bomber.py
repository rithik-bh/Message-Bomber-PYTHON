import os


def clearFile():
    f = open(f"C:\\Users\\{os.getlogin()}\\Desktop\\Message Bomb.txt", "w")
    f.write("")
    f.close()


message = input("Enter Message : ")
times = int(input("Enter No Of Times To Repeat Message : "))

clearFile()


f = open(f"C:\\Users\\{os.getlogin()}\\Desktop\\Message Bomb.txt", "a")

for x in range(times):
    f.write(f"{message}\n")

f.close()


print("\n\nFile Created at Desktop Named \"Message Bomb\"")

input("")
