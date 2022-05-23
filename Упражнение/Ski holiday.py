days=int(input())
nights=days-1
residention=str(input())
rating=str(input())
price_starting=0
price_middle=0
final_price=0
if residention=="room for one person":
    price_starting=18.00*nights
    if rating == "positive":
        final_price=1.25*price_starting
    if rating == "negative":
        final_price=0.9*price_starting
if residention=="apartment":
    price_starting=25.00*nights
    if nights<10:
        price_middle=0.70*price_starting
    elif 10<=nights<=15:
        price_middle=0.65*price_starting
    elif nights>15:
        price_middle=0.50*price_starting
    if rating == "positive":
        final_price = 1.25 * price_middle
    if rating == "negative":
        final_price = 0.9 * price_middle
if residention=="president apartment":
    price_starting=35.00*nights
    if nights<10:
        price_middle=0.90*price_starting
    elif 10<=nights<=15:
        price_middle=0.85*price_starting
    elif nights>15:
        price_middle=0.80*price_starting
    if rating == "positive":
        final_price = 1.25 * price_middle
    if rating == "negative":
        final_price = 0.9 * price_middle
print(format(final_price, ".2f"))