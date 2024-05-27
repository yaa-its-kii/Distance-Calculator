print("______________________________________________________________________")
print("                                                                      ")
print("                          DISTANCE CALCULATOR                         ")
print("______________________________________________________________________")
print("DISTANCE CALCULATOR")
while True:
    x1,y1=list(map(int,input("Enter point 1'sco-ordinates: ").split(",")))
    x2,y2=list(map(int,input("Enter point 2'sco-ordinates: ").split(",")))
    Distance=(((x2-x1)**2)+((y2-y1)**2))**0.5
    print("Distance between the two points = ",round(Distance,3))
    print("<========================================================================>")


    a=input("Do you want to continue or exit? (y/n)")
    if a =="n":
        break


