#lessone if

x = int(input("give me a number less than 10 or equal to 10 :"))
if x <= 10:
    print("thankyou")


#example 2
#write a porgraming that asks for a number less than or equal to 10 but more than or equal to
x = int(input("give me a number more than or equal to 5 and lees or equal to 10 : "))

#we ues somthing called nesting

if x >= 5: #check if it more than or equal to 5
    if x <= 10:#V
        print("thank you ")

#exampel 3
x = int(input("5 <= x <=10 :"))

if x > 10:
    print("too big")
elif x < 5:
    print("too small")
else:
    print("thank you ")


#example 5 do we need elife ?
x = int(input("give me an integer :"))
if x >= 1000:
    print("x is very large")
elif x >= 100 :
    print("x is large ")
elif x >= 10 :
    print("x is a lititle big")
elif x < 10:
    print("perfect ")

#example 6

n = int(input("how many phones do you have "))
if n == 0: #cheak 0
    print("that is soo sad")
elif n == 1: #is it 1 ?
    print("that is normal ")
elif n == 2:#is it 2 ?
    print("that is good")
elif n>= 3: # is it 3,4,5 , .... etc
    print("exllant")
else:
    print("i dont understand")

#part 2
x = int(input("give me a number x , x is more than or equal to 5 and less than or equal to 10 :"))
if x >= 5 and x <=10:
    print("thank you")
else:
    print("no , that is wrong")
`
 #check with and boolena
if x >=5 and x <=10:
    print("thank you")
else:
    print("no , that is worng")


#example
#nesting اقدر اختار بولين او نستق
if x >= 5 and x<=10:
    if x >= 5:
        if x <= 10:
            print("thank you ")
        else:
            print("no  because x need to be <=30")
    else:print("no beacause x needs to be >=5")

#give me an integer >=1 and <= 100 and even x%2 ==0
#راح اكتبها بطريقتين

#boolean way
x = int(input("give me an integer >=1 and <= 100 and even"))
if x >=1 and x <=100 and x%2 == 0:
elif x > 100:
    print("too big")
elif x < 1:
    print("too small")
elif not x%2 == 0:
    print("thai is not even")

#nesting
if x >= 1:
    if x <100:
        if x%2 == 0:
            print("thankyou")
        else:
            print("x is not even")
    else:
        ("too big")
else:
    ("too small")


#we can use nasten and boolean together
if x >=1 and x <=100 and x%2 == 0:
    print("thank you")
else:
    if x < 1:
        print("too small")
    if x > 100:
        print("too big")
    if x%2 ==0:
        print("not even ")
#example
def H(x):
    if x > 0:
        return 1
    elife x ==0:







