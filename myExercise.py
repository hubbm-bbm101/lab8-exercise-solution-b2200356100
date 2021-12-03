import sys
students={}
with open(sys.argv[1],'r') as student :
    for v0 in student :
        data=v0.strip().split(':')
        students[data[0]]=data[1]
    check=sys.argv[2].split(',')
    for v2 in check :
        try :
            print("Name:{},{} ".format(v2,students[v2]))
        except KeyError :
            print("No record of \'{}\' was found! ".format(v2))