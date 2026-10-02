acc = 0; n = input()
import sys
for x in n: 
    if x == "i":
        acc += 1 
    else:
        pass
n.replace("i", "")
for x in n: 
    if x == "d":
        acc -= 1 
    else:
        pass
n.replace("d", "")
for x in n: 
    if x == "s":
        acc **= 2
    else:
        pass
n.replace("s", "")
for x in n: 
    if x == "o":
        print(acc)
    else:
        pass
n.replace("o", "")
for x in n: 
    if x == "h":
        sys.exit()
    else:
        pass
n.replace("h", "")