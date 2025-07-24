#importing libraries
import random
import secrets

#randomise numbers
def randomNum(x,y):
    var=random.randint(x,y)
    return(var)

#randomise letters
def randomLetter():
    alph=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    z=randomNum(0,1)
    w=randomNum(0,25)
    if z==0:
        return alph[w]
    else:
        return (alph[w]).upper()

#randomise special characters
def randomSpecChar(x):
    z=randomNum(0,x-1)
    return alphP[z]

#creating variables/arrays and taking inputs
char=int(input("how many characters are required?"))
num=int(input("how many numbers are required?"))
specChar=int(input("how many special characters are required?"))
unusableChar=input("is there any unusable special characters?")
uc=[]
alphP=["!","£","$","%","&","*","?","-","_"]
lalphp=len(alphP)
password=[]
count=0
finalpassword=[]
numofUC=lalphp+1 
#validating unusableChar input
if unusableChar!="yes":
    if unusableChar!="no":
        print("unusableChar must be either yes or no")
        exit()

#check if there are any special characters that cannot be used
if unusableChar=="yes":
    while numofUC>lalphp:
        numofUC=int(input("how many unusable special characters are there?"))
        if numofUC>lalphp:
            print("there are only", lalphp," special characters", alphP)

#adds all special characters that cannot be used to uc array
    for i in range(numofUC):
        x=input("enter a character you are unable to use:")
        if x in alphP:
            uc.append(x)
        else:
            print("this character is already not available")

#removes all special characters that cannot be used from alphP array
for i in uc:
    alphP.remove(i)

lalphpnew=len(alphP)
x=randomSpecChar(lalphpnew)

#creating the password
for i in range(char):
    n=randomLetter()
    password.append(n)

for i in range(num):
    m=randomNum(0,9)
    password.append(m)

for i in range(specChar):
    k=randomSpecChar(lalphpnew)
    password.append(k)

#securely randomising the letters generated
for i in range(len(password)):
    var5=secrets.choice(password)
    finalpassword.append(var5)
    password.remove(var5)

#outputs the final list as a continuous string
print("your password is: ",''.join(str(i) for i in finalpassword))