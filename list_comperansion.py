num=[1,2,3,4,5,6]
double=[]
for i in num:
    double.append(i*2)
print(double)

# for loop with if loop in list
friends=['rajesh','sam','seema','harish','shital']
start_s=[]
for friend in friends:
    if friend.startswith('s'):
        start_s.append(friend)
print(start_s)

# same output with list comprension

start_s1=[f for f in friends if f.startswith('s')]
print(start_s1)