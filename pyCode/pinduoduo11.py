n = int(input())
for i in range(n):
    z = int(input())
    zoom = int(z//10)
    for j in range(3*zoom):
        inline = input()
    l = input().split()
    s = l[2*zoom]+l[3*zoom]+l[4*zoom]+l[5*zoom]+l[6*zoom]+l[7*zoom]
    if s=='110011':
        for j in range(zoom-1):
            inline = input()
        l = input().split()
        s = l[2*zoom]+l[3*zoom]+l[4*zoom]+l[5*zoom]+l[6*zoom]+l[7*zoom]
        if s=='110011':
            print(0)
            
        elif s=='011110':
            print(8)
            
        elif s=='011111':
            print(9)
        for j in range(6*zoom-1):
            l = input().split()
    elif s=='001100':
        print(1)
        for j in range(7*zoom-1):
            l = input().split()
        continue
    elif s=='000110':
        print(2)
        for j in range(7*zoom-1):
            l = input().split()
        continue
    elif s=='011110':
        print(4)
        for j in range(7*zoom-1):
            l = input().split()
        continue
    elif s=='000011':
        for j in range(zoom-1):
            inline = input()
        l = input().split()
        s = l[2*zoom]+l[3*zoom]+l[4*zoom]+l[5*zoom]+l[6*zoom]+l[7*zoom]
        if s=='011110':
            print(3)
        elif s=='000110':
            print(7)
        for j in range(6*zoom-1):
            l = input().split()
    elif s=='110000':
        for j in range(zoom*2-1):
            inline = input()
        l = input().split()
        s = l[2*zoom]+l[3*zoom]+l[4*zoom]+l[5*zoom]+l[6*zoom]+l[7*zoom]
        if s=='000011':
            print(5)
        if s=='110011':
            print(6)
        for j in range(5*zoom-1):
            l = input().split()

