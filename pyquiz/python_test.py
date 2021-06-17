


x=[100,110,120,130,140,150]
for b in x:
    c=[b*5 for b in x]
    print(c)


    def divisible_by_three(n):
       for x in range(1,n):
        if(x%3==0):
            print(x)
divisible_by_three(32)
divisible_by_three(32)


x=[[1,2],[3,4],[5,6]]
y=[]
for k in x:
    for l in k:
        y.append(l)
print(y)


# a=([3,6,8,2,4,1,5,7])
# smallest=list(a)
# print(smallest)

# def smallest():
#     numbers=[3,6,8,2,4,1,5,7]
#     smallestvalue=smallest(numbers)
#     print(smallest)

def smallest(i):
    print(min(i))
smallest([1,3,4,7,45,5,40])



def remove_duplicate(x):
    p=set(x)
    print(p)
remove_duplicate(x = ['a','b','a','e','d','b','c','e','f','g','h'])




def  divisible_by_seven():
    for y in range(100,200):
        if y%7==0:
            print(y)
divisible_by_seven()










