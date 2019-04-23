T = int(input())

case_no = 1

for i in range(T):

    a = int(input())
    b = int(input())
    sum = 0
    for j in range(a, b+1, 1):
        if j%2==1:
            sum+=j

    print("Case %d: %d" %(case_no, sum))
    case_no+=1