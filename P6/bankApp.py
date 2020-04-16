'''
Description: Bank application that allows user to deposit, withdraw, display balance, and change user
Written by: Dong Hyun Lee
Date: Dec 9 2018
'''

userName=['Mike', 'Jane', 'Steve']
balances=[300,400,500]
l=balances





a=input('What is your user name? ')
if a not in userName:
    while a not in userName:
        a=input('INVALID user name. Please enter your user name again: ')
        if a in userName:
            x=l[userName.index(a)]
else:
    x=l[userName.index(a)]





b=input('<MENU> Please choose one of the options (Type D to deposit money)  (Type W to withdraw money)  (Type B to display Balance)  (Type C to change user, display user name)  (Type E to exit) ').upper()





def Deposit(d):
    return(displayBalance(x+d))
    
def Withdraw(w):
    return(displayBalance(x-w))
    
def displayBalance(s):
    return(s)



if b!='D' and b!='W' and b!='B' and b!='C' and b!='E':
    while b!='D' and b!='W' and b!='B' and b!='C' and b!='E':
        print('INVALID OPTION')
        b=input('<MENU> Please choose one of the options (Type D to deposit money)  (Type W to withdraw money)  (Type B to display Balance)  (Type C to change user, display user name)  (Type E to exit) ').upper()
            

while b!='E':
    if b=='D':
        g=float(input('Enter the amount to deposit: '))
        if g<0:
            print('INVALID INPUT. Please enter a positive value')
        else:
            print('New Balance is : '+str(Deposit(g)))
            x+=g
            l[userName.index(a)]=x
            

      
        b=input('<MENU> Please choose one of the options (Type D to deposit money)  (Type W to withdraw money)  (Type B to display Balance)  (Type C to change user, display user name)  (Type E to exit) ').upper()
        if b!='D' and b!='W' and b!='B' and b!='C' and b!='E':
            while b!='D' and b!='W' and b!='B' and b!='C' and b!='E':
                print('INVALID OPTION')
                b=input('<MENU> Please choose one of the options (Type D to deposit money)  (Type W to withdraw money)  (Type B to display Balance)  (Type C to change user, display user name)  (Type E to exit) ').upper()
                    

    
    
    
    elif b=='W':
        h=float(input('Enter the amount to withdraw: '))
        if h<0:
            print('INVALID INPUT. Please enter a positive value')
        else:
            if h>x:
                print ('not enough balance')
            else:
                print('New Balance is: '+str(Withdraw(h)))
                
                x-=h
                l[userName.index(a)]=x
            
        b=input('<MENU> Please choose one of the options (Type D to deposit money)  (Type W to withdraw money)  (Type B to display Balance)  (Type C to change user, display user name)  (Type E to exit) ').upper()
        if b!='D' and b!='W' and b!='B' and b!='C' and b!='E':
                    while b!='D' and b!='W' and b!='B' and b!='C' and b!='E':
                        print('INVALID OPTION')
                        b=input('<MENU> Please choose one of the options (Type D to deposit money)  (Type W to withdraw money)  (Type B to display Balance)  (Type C to change user, display user name)  (Type E to exit) ').upper()
                            
    
    
    
    
    
    elif b=='B':
        print('Your Balance is : '+str(displayBalance(x)))
        
        b=input('<MENU> Please choose one of the options (Type D to deposit money)  (Type W to withdraw money)  (Type B to display Balance)  (Type C to change user, display user name)  (Type E to exit) ').upper()
        if b!='D' and b!='W' and b!='B' and b!='C' and b!='E':
            while b!='D' and b!='W' and b!='B' and b!='C' and b!='E':
                print('INVALID OPTION')
                b=input('<MENU> Please choose one of the options (Type D to deposit money)  (Type W to withdraw money)  (Type B to display Balance)  (Type C to change user, display user name)  (Type E to exit) ').upper()
                    
        
    
    
    
    
    elif b=='C':
        a=input('What is your user name? ')
        if a not in userName:
            while a not in userName:
                a=input('INVALID user name. Please enter your user name again: ')
                if a in userName:
                    x=l[userName.index(a)]
        else:
            x=l[userName.index(a)]
        b=input('<MENU> Please choose one of the options (Type D to deposit money)  (Type W to withdraw money)  (Type B to display Balance)  (Type C to change user, display user name)  (Type E to exit) ').upper()
        if b!='D' and b!='W' and b!='B' and b!='C' and b!='E':
            while b!='D' and b!='W' and b!='B' and b!='C' and b!='E':
                print('INVALID OPTION')
                b=input('<MENU> Please choose one of the options (Type D to deposit money)  (Type W to withdraw money)  (Type B to display Balance)  (Type C to change user, display user name)  (Type E to exit) ').upper()
                
                
                

