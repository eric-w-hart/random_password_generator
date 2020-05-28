import random


def guessPassw(guess):
    if guess =='weak':
        password=(''.join([random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))for x in range (8)]))
    elif guess=='medium':
        password=(''.join([random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))for x in range (10)]))
    elif guess=='strong':
        password=(''.join([random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM.!#$*,.?&%'))for x in range (14)]))
    else:
       print('ERROR')
       guess=input('How strong do you want the password weak/medium/strong : ')
       password=guessPassw(guess)
    return password 
       

def informationAboutPassword(a):
    countNumber=0
    countLower=0
    countUpper=0
    listUpperLetter=[]
    listLowerLetter=[]
    listNumber=[]
#    print("The size of your password = {}".format(len(a)))
#    print ('- - -'*5)
#    print("Your password starts with = {}".format(a[0]))
#    print ('- - -'*5)
#    print("The end of your password  = {}".format(a[-1]))
#    print ('- - -'*5)
    print("Your password = {} ".format(a))
    print ('- - -'*5)
    
    for j in range(0,len(a)):
        for i in ['0','1','2','3','4','5','6','7','8','9']:
            if(a[j]==i):
               listNumber.append(i)
               countNumber=countNumber+1
                
#    print ("Number of digits in the password ={} ".format(countNumber))
#    print("Your password has digits={}".format(listNumber))
#    print ('- - -'*5)

    for j in range(0,len(a)):
        for i in ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']:
            if(a[j]==i):
                listLowerLetter.append(i)
                countLower=countLower+1
                
#    print ("Number of lower case letters in the password = {}".format(countLower))
#    print("Your password has a lower case letter = {}".format(listLowerLetter))
#    print ('- - -'*5)
    
    for j in range(0,len(a)):
        for i in ['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']:
            if(a[j]==i):
                listUpperLetter.append(i)
                countUpper=countUpper+1
                
    
#    print ("Number of upper case letters  in the password = {}".format(countUpper))
#    print("Your password has a upper case letter ={}".format(listupperLetter))
#    print ('- - -'*5)
    
def randHello():
    print('Hello, friend :)')
    name=input('What is your name ? ')
    print('{} ,nice to meet you '.format(name))
    
randHello()
guess=input('How strong do you want the password weak/medium/strong : ')
yourPassword=guessPassw(guess)
question= input('Do you want your password on screen (yes/no)?')
if (question == 'yes'):
            informationAboutPassword(yourPassword)
else:
             print('See you later :)')
