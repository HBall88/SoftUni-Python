shirt_price=float(input())
needed_sum=float(input())
shorts_price=0.75*shirt_price
socks_price=0.2*shorts_price
sum1=shirt_price+shorts_price
shoes_price=2*sum1
sum2=shirt_price+shorts_price+socks_price+shoes_price
sum_ready=0.85*sum2
diff=sum_ready-needed_sum
if diff>=0:
    print(f"Yes, he will earn the world-cup replica ball!")
    print(f'His sum is {format(sum_ready, ".2f")} lv.')
else:
    print("No, he will not earn the world-cup replica ball.")
    print(f'He needs {format(abs(diff), ".2f")} lv. more.')