import os
from playsound import playsound
import datetime
import subprocess
import platform
import rlcompleter, readline
readline.parse_and_bind('tab: complete')
start = """
\033[1;32;40m
  ================ | Stalin Junior Development © | ==================
  █████   ██████   █████   ██      ██  ███   ██         █████   █████
  ██        ██    ██   ██  ██      ██  ████  ██        ██   ██  ██
  █████     ██    ███████  ██      ██  ██ ██ ██  ████  ██   ██  █████
     ██     ██    ██   ██  ██      ██  ██  ████        ██   ██     ██
  █████     ██    ██   ██  ██████  ██  ██   ███         █████   █████

"""
print(start)
playsound("welcomesound.mpga")
password = "stalinjunior"
login = input("password?: ")
if login == password : ## you should change here to take password control from database or json like data structure.
    print("welcome sir")
    def ret():
        process = input("what do you want to do?: ")
        if process == "":
            print("please do not leave empty")
        elif process == "date":
            date = datetime.datetime.now()
            print("Date and Time: ", date)
        elif process == "ping":
            ping = input("url?: ")
            response = os.system("ping -c 1 " + ping)
        elif process == "calculator":
            def gather(x, y):
                return x + y
            def interest(x, y):
                return x - y
            def multiply(x, y):
                return x * y
            def divide(x, y):
                return x / y
            print("select action to do")
            print("================ | Stalin Junior Development © | ==================")
            print("1 = gather")
            print("2 = interest")
            print("3 = multiply")
            print("4 = divide")
            print("================ | Stalin Junior Development © | ==================")
            choice = input("your choice (1, 2, 3 or 4): ")
            number1 = int(input("1: "))
            number2 = int(input("2: "))
            if choice == '1':
                print(number1,"+",number2,"=", gather(number1,number2))
            elif choice == '2':
                print(number1,"-",number2,"=", interest(number1,number2))
            elif sechoicecim == '3':
                print(number1,"*",number2,"=", multiply(number1,number2))
            elif choice == '4':
                print(number1,"/",number2,"=", divide(number1,number2))
            else:
                print("error!")
        elif process == "terminal":
            terminal = input("=>$ ")
            os.system(terminal)
        elif process == "system details":
            print(platform.machine(), "\n")
            print(platform.version(), "\n")
            print(platform.platform(), "\n")
            print(platform.uname(), "\n")
            print(platform.system(), "\n")
            print(platform.processor(), "\n")
        ret()
    ret() 
elif login == "31":
    print("sj")
elif login == "":
    print("please do not leave empty")
else:
    print("wrong password!")
    
if __name__ == "__main__":
    main()
