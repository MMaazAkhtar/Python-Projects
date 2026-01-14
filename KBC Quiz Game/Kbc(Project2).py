import sys

e="Wrong Answer\n"
f="Correct Answer!\n"
x=1000
y=x+1000
def score(x):
    print("Your prize is:\n",x,"$\n")

def total_prize(x):
    
    print("Your total prize is:\n",x,"$\n")
def stop(e):
    sys.exit(f"Program exited!\nNice Try\nHope you complete next time")





        
def quiz(a,b,c,d,answer,e,f):
        
        print(a,"\n",b,"\n",c,"\n",d,"\n")
        select=input("Select Answer(type option alphabet):")
        match select:
            case'a':
                print(a)
                if a==answer:
                    print(f)
                else:
                    print(e)
                    stop(e)
            
            case'b':
                print(b)
                if b==answer:
                    print(f)
                else:
                    print(e)
                    stop(e)
            case'c':
                print(c)
                if c==answer:
                    print(f)
                else:
                    print(e)
                    stop(e)
            case'd':
                print(d)
                if d==answer:
                    print(f)
                else:
                    print(e) 
                    stop(e)
            case __:
                print("Invalid Input")
                quiz(a,b,c,d,answer,e,f)
                

KBC="***WELCOME_TO_KBC*** "
print(KBC.center(150))
questions=["1.Which is the largest country in the world?\n","2.How much percent of the earth is water?","3.Zurich is the capital of:","4.Python is a:"
           "5.Chess is a mandatory subject in:","6.Which planet is known as the 'Red Planet'?",""]#questions[1]

print(questions[0])
a="a)Russia"
b="b)US"
c="c)Canada"
d="d)China"
answer="a)Russia"
quiz(a,b,c,d,answer,e,f)
score(x)

print(questions[1])
a="a)50%"
b="b)70%"
c="c)60"
d="d)80%"
answer="b)70%"
quiz(a,b,c,d,answer,e,f)
total_prize(2000)

print(questions[2])
a="a)Austria"
b="b)Iceland"
c="c)Switzerland"
d="d)Belgium"
answer="c)Switzerland"
quiz(a,b,c,d,answer,e,f)
total_prize(3000)

print(questions[3])
a="a)General Purpose Language"
b="b)Special Purpose Language"
c="c)Compiled Language"
d="d)Interpreted Language"
answer="d)Interpreted Language"
quiz(a,b,c,d,answer,e,f)
total_prize(4000)

print(questions[4])
a="a)Azerbaijan"
b="b)Armenia"
c="c)Georgia"
d="d)Russia"
answer="b)Armenia"
quiz(a,b,c,d,answer,e,f)
total_prize(5000)

print(questions[5])
a="a)Venus"
b="b)Mars"
c="c)Jupiter"
d="d)Saturn"
answer="b)Mars"
quiz(a,b,c,d,answer,e,f)
total_prize(6000)

print(questions[6])
a="a)Venus"
b="b)Mars"
c="c)Jupiter"
d="d)Saturn"
answer="b)Mars"
quiz(a,b,c,d,answer,e,f)
total_prize(7000)
print("Congratulations!\nYou take home 4000$\nCREDITS:\nDeveloper:'Maaz Akhtar'")
