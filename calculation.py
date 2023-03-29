n=float(input("select your choice 1:acre to guntas 2 :guntas to acres\n"))
m=int(input("how many different places you have land "))
print("enter your land in different places one by one")
total_area=0
#total_acres=0
for l in range(0 , m):
    if(n==1):
        acre=float(input("enter your area in acres"))
        guntas=acre*40
        #print("your area in guntas is", guntas)
        total_area=total_area+guntas

    elif(n == 2):
        guntas = float(input("enter your area in guntas"))
        total_acre = guntas / 40
        total_area=total_area+total_acre
print("your total area is",total_area)















