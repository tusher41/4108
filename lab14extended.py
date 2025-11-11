def extended_gcd(a,b):
 if a == 0:
     return b, 0, 1
 g, x1, y1=extended_gcd(b%a, a)
 return g, y1- (b//a) *x1, x1

def mod_inverse(a,m):
     g, x, _ = extended_gcd(a, m)
     return x % m if  g==1 else None
    
a,m=7,26
g,x,y=extended_gcd(a,m)
print("GCD:",g)
print("x,y:",x,y)
print("Moduler inverse of",a,"mod",m,"is:",mod_inverse(a,m))