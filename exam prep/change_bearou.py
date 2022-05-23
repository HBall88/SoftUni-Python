bitcoins=int(input())
chinese_coins=float(input())
comission=float(input())/100
bitcoin_to_leva=bitcoins*1168
chinese_coins_to_dollars=chinese_coins*0.15
chinese_coins_to_leva=chinese_coins_to_dollars*1.76
sum_in_leva=bitcoin_to_leva+chinese_coins_to_leva
sum_in_euro=sum_in_leva/1.95
sum_for_printing=sum_in_euro-comission*sum_in_euro
print(format(sum_for_printing, ".2f"))