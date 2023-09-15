a=int(input())
b=int(input())
c=int(input())
import math
d=float(math.sqrt(b**2-4*a*c))
ans1=(-b+d)/2*a
ans2=(-b-d)/2*a
print(ans1,ans2)