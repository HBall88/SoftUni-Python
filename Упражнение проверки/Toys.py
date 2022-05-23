excursion_price=float(input())
jigsaw_count=int(input())
dolls_count=int(input())
teddies_count=int(input())
miniouns_count=int(input())
trucks_count=int(input())
totcount=jigsaw_count+dolls_count+teddies_count+miniouns_count+trucks_count
totprice=jigsaw_count*2.60+dolls_count*3+teddies_count*4.10+miniouns_count*8.20+trucks_count*2
if totcount>=50:
    totpricec=totprice-0.25*totprice
    totprice1=totpricec-0.1*totpricec
    if totprice1>=excursion_price:
        f=totprice1-excursion_price
        print(f'Yes! {format(f, ".2f")} lv left.')
    if totprice1<excursion_price:
        f=excursion_price-totprice1
        print(f'Not enough money! {format(f, ".2f")} lv needed.')
if totcount<50:
    totprice1=totprice-0.10*totprice
    if totprice1>=excursion_price:
        f=totprice1-excursion_price
        print(f'Yes! {format(f, ".2f")} lv left.')
    if totprice1<excursion_price:
        f=excursion_price-totprice1
        print(f'Not enough money! {format(f, ".2f")} lv needed.')