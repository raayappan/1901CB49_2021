def get_memory_score(l):
    a=[]
    count=0
    for i in l:
        if i in a:
            count+=1
        else:
            a.append(i)
            if len(a)>5:
                a.pop(0)
    #print(a)
    return count

input_nums = []
c=0
inv=[]
for i in input_nums:
    if(type(i)!=int):
        c+=1
        inv.append(i)
if c!=0:
    print("Please enter a valid input list. Invalid inputs detected:",inv)
else:
    print("Score: ",get_memory_score(input_nums))
