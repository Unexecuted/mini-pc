def welcome():
  print("Welcome to mini pc! Use the PC_ON and PC_OFF commands to turn the pc on and off, and the help command to generate a list of current commands!\n")

def my_help():
  ask = input('What would you like help with?\n1. Commands list\n2. Bug Reporting\n3. Apps\n')
  if ask == '1' or ask == '1.':
    print('PC_OFF, help, echo, forgot_pass, battery')

def echo(user):
  print(user)

def forgot_pass(user):
  return 1

def commands(command):
  if 'echo ' in command[:5]:
    echo(command[5:])

def battery(battery):
  print('Battery: ' + str(battery) + '%')

def change_color(color, background):
  print('test')