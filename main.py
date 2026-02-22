user_0 = {
'username': 'efermi',
'first': 'enrico',
'last': 'fermi',
}
test = [['a','b','c'],['e','f','d']]
test1=''
for i in test:
    print(i)
    i.sort()
    for j in i:
        print(j)
        test1+=j
test.append(['k'])
for value in range(1,6):
    print(value)
numbers = list(range(1,7))
# print even numbers
numbers = list(range(1,7,2))
squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)

print(squares)
print(numbers)
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[2:])
print(players[-3::2])
# copying a list
playercopy = players[:]
print(test)
print(test1)

for name in user_0.items():
    # print("key",key)
    # print("\n Value",value)
    print(name)

for name in sorted(user_0.keys()):
    print(name)
for value in sorted(user_0.values()):
    print(value)


def build_profile(first,last, **user_info):
    profile ={}
    profile['first name'] =first
    profile['last name']= last
    for key,value in user_info.items():
        profile[key] =value
    return profile

user_profile = build_profile('albert','einstein',location ='princeton',field ='physics')
print(user_profile)


class dog():
    def __init__(self,name,age):
        self.name =name
        self.age = age

    def sit(self):
        print(self.name.title()+" is now sitting")

    def roll_over(self):
        print(self.name.title()+"rolled over")

my_dog = dog('willie',6)
print("my dog's name is " +my_dog.name+".")
print("my dog is "+ str(my_dog.age) +" Years old")


a= [[1,2,3,4,5],[5,6,7,8,9]]
b=[]
for i in a:
    for j in i:
        b.append(j)
print(b)





