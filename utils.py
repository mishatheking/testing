def find_max(list):
    Max=list[0]
    for i in list:
        if i > Max:
            Max=i
    print(Max)

find_max([1,2,3,4,5,6,9])