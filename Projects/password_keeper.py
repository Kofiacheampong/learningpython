from cryptography.fernet import Fernet
from cryptography.fernet import InvalidToken


# key + password + text to encrypt = random text
# random text + key + password = text to encrypt

def write_key():
   key = Fernet.generate_key()
   with open ('key.key','wb') as key_file:
      key_file.write(key)
write_key()

def load_key():
   file = open('key.key', 'rb')
   key = file.read()
   file.close()
   return key

master_pwd = input('Whats the master password? ')

key = load_key() 
fer = Fernet(key)

def view() -> None:
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            line = line.strip()  # Remove leading/trailing whitespace
            if line:  # Skip empty lines
                user, passw = line.split('|')
                try:
                  print(f'User: {user} | Password: {fer.decrypt(passw.encode()).decode()}')
                except InvalidToken as e:
                   print(f'Invalid Master Password{e}')
               

def add():
    name = input('Account name: ')
    pwd = input('password: ')
    with open('passwords.txt', 'a') as f:
        f.write(f'{name}|{fer.encrypt(pwd.encode()).decode()}\n')

while True:
   mode = input('Add new password or view existing? ')

   if mode == 'q': 
      quit()
   if mode == 'view':
      view()
   elif mode == 'add':
      add()
   else:
      print('Invalid mode')
   
      
