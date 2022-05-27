key=int(input())
n=int(input())
decrypted_word=""
for _ in range(n):
    sym=str(input())
    sym1=ord(sym)
    d_sym=chr(sym1+key)
    decrypted_word+=d_sym
print(decrypted_word)