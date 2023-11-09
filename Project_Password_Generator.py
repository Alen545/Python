import random
input('Welcome to the Password Generator!!!')
letter = int(input('How many letter would you like in your password?'))
symbol = int(input('How many symbols would you like?'))
number = int(input('How many number would you like?'))

letterValue = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W',
               'X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t',
               'u','v','w','x','y','z']
symbolValue = ['!','@','#','$','%','^','&','*','(',')','~']
numberValue = [0,1,2,3,4,5,6,7,8,9]
passwordList = []
for x in range(letter):
     char = random.choice(letterValue)
     passwordList.append(char)
for x in range(symbol):
    char = random.choice(symbolValue)
    passwordList.append(char)
for x in range(number):
    char = random.choice(numberValue)
    passwordList.append(str(char))
random.shuffle(passwordList)
print(passwordList)
password = ''.join(map(str,passwordList))
print(password)








