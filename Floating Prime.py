


def check_prime(test):  
    numbers=[int(test*10),int(test*100),int(test*1000)]
    for num in numbers:
        if num>1:
            for i in range(2,num):
                if (num%i)==0:
                    break
            else:
                return True
    return False

        
def get_input():
    #emp_list=list()
    test=float(input("Please Enter Number:"))
    while test!=0.0:
        #emp.append(test)
        print(check_prime(test))
        test=float(input("Please Enter Number:"))



get_input()