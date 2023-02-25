S=set()

def add(i):
    S.add(i)

def remove(i):
    S.remove(i)

def check(i):
    if i in S:
        return 1
    else:
        return 0

def toggle(i):
    if i in S:
        S.remove(i)
    else:
        S.add(i)

def empty():
    S.clear()

