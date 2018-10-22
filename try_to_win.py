from random import randint
    
def computer_input(count):
    target_list=[2,5,8,11,14,17,20]
    if count+1 in target_list:
        return 1
    elif count+2 in target_list:
        return 2
    else:
        return randint(1, 2)


count =0
user_name= raw_input('Please enter your name: ')
computer_name= raw_input('Computer user name: ')
print "-----------------------------------------------------"
print {"Rules" :" You can enter 1 or 2 and win the game which will reach 20! Let's Play"}
print '------------------------------------------------------'
while count<20:
    user_input= input("user: ")
    while(not user_input in [1,2]):
        print 'wrong input please selecte either 1 or 2'
        user_input= input("user: ")
        
    count = count + user_input
    print 'count: ',count
    name = user_name
    computer_user= computer_input(count)
    count =count+computer_user
    print "computer: ", str(computer_user), "count: ", str(count)
    name= computer_name
    
if count==20:
    print '------congratulations-----'
    print 'winner is \n ', name
    
