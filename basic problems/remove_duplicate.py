def remove_duplicate(items):
    unique=[]
    for item in items:
        if item not in unique:
            unique.append(item)
    return unique

numbers=[22,12,2,2,5,4,2,3,5,8,2,5,7,2,8,6,996,69,2,3,69,6]
print(remove_duplicate(numbers))