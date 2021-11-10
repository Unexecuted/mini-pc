import smtplib

#'terminal' commands
def welcome():
  print("Welcome to mini pc! Use the PC_ON and PC_OFF commands to turn the pc on and off, and the help command to generate a list of current commands!\n")

def my_help():
  ask = input('What would you like help with?\n1. Commands list\n2. Bug Reporting\n3. Apps\n')
  if ask == '1' or ask == '1.':
    print('PC_OFF, help, echo, forgot_pass, battery')

def echo(message):
  print(message)

def forgot_pass(user):
  return 1

def commands(command):
  if 'echo ' in command[:5]:
    echo(command[5:])

def battery(battery):
  print('Battery: ' + str(battery) + '%')

def change_color(color, background):
  print('test')


#apps
def email(sendto, message):
  email = 'replitfeedback@gmail.com' # Your email
  password = 'replitfeedback12' # Your email account password
  send_to_email = str(sendto) # Who you are sending the message to

  server = smtplib.SMTP('smtp.gmail.com', 587) # Connect to the server
  server.starttls() # Use TLS
  server.login(email, password) # Login to the email server
  server.sendmail(email, send_to_email , message) # Send the email
  server.quit() # Logout of the email server