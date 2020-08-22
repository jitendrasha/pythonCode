def linearSearxh(a,key):
    position=0
    flag=False
    while position<len(a) and not flag:
        if a[position]==key:
            flag=True
        else:
                position=position+1
    return flag


a=[84,21,47,96,15]
found=linearSearxh(a,47)
print('element  47 is present:',found)