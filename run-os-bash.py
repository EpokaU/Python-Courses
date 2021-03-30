import os

command = os.popen('ls -al')
print(command.read())
print(command.close())
