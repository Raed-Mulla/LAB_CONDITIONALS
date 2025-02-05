movie:str = "End Game"
rating:int = int(input("Enter rating out of 5 :"))
score:float = float(input("enter score out of 100 :"))

if rating >= 4 and score >= 80:
    print("Highly recommended")
elif rating >= 3 and score >= 70:
    print("I recommended it . It is good")
elif rating >= 2 and score >= 60:
    print("You should check it out")
else:
    print("Don't watch it. It is a waste of time")
