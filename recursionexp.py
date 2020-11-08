'''
when a function calls itself it is called recursion

'''
import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(2000)
i=0
def msg():
    global i
    print(i,"Good Morninng")
    i=i+1
    msg()

msg()
msg()