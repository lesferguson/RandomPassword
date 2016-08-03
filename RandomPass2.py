import string
import random

# Global definitions for character choice
#               0                       1                    2                                   3                                             4             
characters = [string.ascii_lowercase, string.ascii_letters, string.ascii_letters + string.digits, string.ascii_letters + string.digits + '!@#$_', string.ascii_letters + string.digits + string.punctuation]

def PasswordGenerator(length=8, complication=4, force=True):
    # Function to actually generate the password
    # complication: 
    # 0 = lowercase letters
    # 1 = and uppercase letters
    # 2 = and numbers
    # 3 = and !@#$_
    # 4 = and "%&'()*+,-./:;<=>?[\]^`{|}~
    
    # Variables called later
    password_list = []
    character_checks = {'upper':False, 'lower':False, 'digit':False, 'symbol':False}
    

    for _ in range(0, length, 1):
        password_list.append(random.SystemRandom().choice(characters[complication]))
    if force == 'y':
        character_checks = CharacterCheck(password_list, complication)
        if complication == 4:
            while character_checks['upper']==False or character_checks['lower']==False or character_checks['digit']==False or character_checks['symbol']==False:
                password_list = CharacterReplace(password_list, character_checks, complication) #Replace characters to try and ensure it has all of the types
                character_checks = CharacterCheck(password_list, complication)                  #Verify if the password is now good
        if complication == 3:
            while character_checks['upper']==False or character_checks['lower']==False or character_checks['digit']==False or character_checks['symbol']==False:
                password_list = CharacterReplace(password_list, character_checks, complication) #Replace characters to try and ensure it has all of the types
                character_checks = CharacterCheck(password_list, complication)                  #Verify if the password is now good
        if complication == 2:
            while character_checks['upper']==False or character_checks['lower']==False or character_checks['digit']==False:
                password_list = CharacterReplace(password_list, character_checks, complication) #Replace characters to try and ensure it has all of the types
                character_checks = CharacterCheck(password_list, complication)                  #Verify if the password is now good
        if complication == 1:
            while character_checks['upper']==False or character_checks['lower']==False:
                password_list = CharacterReplace(password_list, character_checks, complication) #Replace characters to try and ensure it has all of the types
                character_checks = CharacterCheck(password_list, complication)                  #Verify if the password is now good
                
        # No need to check complication 0, since it only has the one type
    else:
        pass
        
        
                
    return ''.join(password_list)
    
    
        
def CharacterCheck(password_list, complication):
    # Function to check if all of the required characters are present in the password.
    
    character_checks = {'upper':False, 'lower':False, 'digit':False, 'symbol':False}
    
    if complication == 4:
        for i in range(0, len(password_list), 1):
            if password_list[i] in string.punctuation:
                character_checks['symbol'] = True
                break
    if complication == 3:
        for i in range(0, len(password_list), 1):
            if password_list[i] in '!@#$_':
                character_checks['symbol'] = True
                break                
    if complication >= 2:
        for i in range(0, len(password_list), 1):
            if password_list[i] in string.digits:
                character_checks['digit'] = True
                break
    if complication >= 1:
        for i in range(0, len(password_list), 1):
            if password_list[i] in string.ascii_uppercase:
                character_checks['upper'] = True
                break
    if complication >= 0:
        for i in range(0, len(password_list), 1):
            if password_list[i] in string.ascii_lowercase:
                character_checks['lower'] = True
                break
    
    return character_checks

def CharacterReplace(password_list, character_checks, complication):
    #Function to actually perform the character replacement
    if complication == 4:
        if character_checks['symbol'] == False:
            password_list[random.randint(0,len(password_list)-1)] = random.SystemRandom().choice(string.punctuation)
        
    if complication == 3:
        if character_checks['symbol'] == False:
            password_list[random.randint(0,len(password_list)-1)] = random.SystemRandom().choice('!@#$_')
                     
    if complication >= 2:
        if character_checks['digit'] == False:
            password_list[random.randint(0,len(password_list)-1)] = random.SystemRandom().choice(string.digits)
        
    if complication >= 1:
        if character_checks['upper'] == False:
            password_list[random.randint(0,len(password_list)-1)] = random.SystemRandom().choice(string.ascii_uppercase)
        
    if complication >= 0:
        if character_checks['lower'] == False:
            password_list[random.randint(0,len(password_list)-1)] = random.SystemRandom().choice(string.ascii_lowercase)
        
    return password_list


user_length = int(raw_input("Please enter the length of the password (Minumun 5: "))
while user_length <5:
    user_length = int(raw_input("Please enter the length of the password (Minumun 5: "))
user_complication = int(raw_input("Please enter the complication requirements\nNote: 0 = lowercase letters\n1 = and uppercase letters\n2 = and numbers\n3 = and !@#$_\n4 = and \"%&\'()*+,-./:;<=>?[\]^`{|}~\n: "))
while user_complication < 0 or user_complication > 4:
    user_complication = int(raw_input("Please enter the complication requirements\nNote: 0 = lowercase letters\n1 = and uppercase letters\n2 = and numbers\n3 = and !@#$_\n4 = and \"%&\'()*+,-./:;<=>?[\]^`{|}~\n: "))
user_force = raw_input("Should passwords require all character types be present (y/n): ")
while user_force != 'y' and user_force != 'n':
    user_force = raw_input("!! ENTRY MUST BE y or n !!\nShould passwords require all character types be present (y/n): ")
    
    
print PasswordGenerator(length=user_length, complication=user_complication, force=user_force)
