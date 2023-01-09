def simpleInterest(p,r,t):
    si=(p*r*t)/100
    return si

def finalAmount(si,prin):
    return si+prin



if __name__ == '__main__':
    p= int(input("enter principle= "))
    r= float(input("enter rate= "))
    t= int(input("enter time= "))

    a=simpleInterest(p,r,t)

    print("simple interst is: ", a)

    print("your final amount is :", finalAmount(a,p))







