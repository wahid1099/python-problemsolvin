def margeList(first,second):
    combined=first+second
    combined.sort()
    return combined



group=[11,13,18,17,56]
group1=[23,15,19,43,66]
merged=margeList(group,group1)
print(merged)