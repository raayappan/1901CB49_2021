def meraki_helper(n):
    pr= -1
    while(n):
        cur=n%10
        if pr== -1:
            pr=cur
        else:
            if abs(pr-cur)!=1:
                return False
        pr=cur
        n//=10
    return True

input = [12, 14, 56, 78, 98, 54, 678, 134, 789, 0, 7, 5, 123, 45, 76345, 987654321]
a=0
b=0
for i in range(len(input)):
    if meraki_helper(input[i])==True:
        print("Yes -",input[i],"is a Meraki number")
        a+=1
    else:
        print("No -",input[i],"is not a Meraki number")
        b+=1
print("the input list contains",a,"Meraki numbers and",b,"non-Meraki numbers.")    