import time
import getpass
import keyring
import random
import termcolor
import replit
from commands import welcome, echo, commands, my_help, battery

def main():
  welcome()

  pc = False

  while pc == False:
    response = input("")
    if response == "PC_ON":
      pc = True
      print("\nPC Successfully Started!")
    elif response == "PC_OFF":
      print("\nPC is not yet on...")

  while pc == True:
    bat_level = 100
    user_list = []
    pass_list = []

    if user_list == []:
      logged_in = False
      print('\nSince this is your first time logging on, please create a new Username and Password.\n')

    login_info = {'Usernames' : [], 'Passwords' : []}
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    user_list.append(username)
    pass_list.append(password)

    login_info['Usernames'] = user_list
    login_info['Passwords'] = pass_list
    logged_in = True
    print(login_info)

    while logged_in == True:
      cmd = input(">")
      if 'echo' in cmd[:5]:
        if 'echo ' in cmd[:5]:
          commands(cmd)
        else:
          print('Missing argument: echo (input)')
      elif 'PC_OFF' in cmd:
        logged_in = False
        pc = False
      elif 'help' in cmd[:4]:
        my_help()
      elif 'clear' in cmd[:5]:
        replit.clear()
      elif 'battery' in cmd[:7]:
        battery(bat_level)
      else:
        print('Unrecognized command; Please try again or type help for a list of commands.')
      bat_level -= 1
      if bat_level == 0:
        pc = False

if __name__ == "__main__":
  main()