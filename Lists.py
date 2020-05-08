lists = []
n = int(input())
for i in range(n):
    a = input().split()
    if len(a) == 3:
        eval("lists." + a[0] + "(" + a[1] + "," + a[2] + ")")
    elif len(a) == 2:
        eval("lists." + a[0] + "(" + a[1] + ")")
    elif a[0] == "print":
        print(lists)
    else:
        eval("lists." + a[0] + "()")
