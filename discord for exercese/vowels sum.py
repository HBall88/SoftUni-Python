a=str(input())
sum_vowels=0
for i in a:
    if i=="a":
        sum_vowels+=1
    if i=="e":
        sum_vowels+=2
    if i=="i":
        sum_vowels+=3
    if i=="o":
        sum_vowels+=4
    if i=="u":
        sum_vowels+=5
print(sum_vowels)