import math

p = int(input("Enter p: "))
q = int(input("Enter q: "))

n = p * q
print("n:", +n)

phi_n = (p - 1) * (q - 1)
print("phi(n):", phi_n)

for e in range(2, phi_n):
    if math.gcd(e, phi_n) == 1:  
        break

print("Selected e:", e)


m = int(input("Enter m: "))

d = pow(e, -1, phi_n)
print("d is:", d)

print(f"Public Key (e, n): ({e}, {n})")
print(f"Private Key (d, n): ({d}, {n})")


C = pow(m, e, n)
print("Ciphertext (C):", C)


M = pow(C, d, n)
print("Decrypted Message (M):", M)
