def SieveOfEratosthenes(n): 
      
    prime = [True for i in range(n+1)] 
    p = 2
    final = []
    while (p * p <= n): 
          
        if prime[p]: 
            final.append(p)
              
            for i in range(p * p, n+1, p): 
                prime[i] = False
        p += 1
        
    return prime

def get_primes(n):
    pr = [1]
    primes = SieveOfEratosthenes(n)
    return [i for i in range(2, len(primes)) if primes[i]]

print(get_primes(100))