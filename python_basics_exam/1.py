fat_percent=int(input())/100
proteins_percent=int(input())/100
carbons_percent=int(input())/100
calories_total=int(input())
water_percentage=int(input())/100
fat_grams=(fat_percent*calories_total)/9
proteins_grams=(proteins_percent*calories_total)/4
carbons_grams=(carbons_percent*calories_total)/4
sum_grams=fat_grams+proteins_grams+carbons_grams
one_gram_calories=calories_total/sum_grams
print_calories=one_gram_calories-water_percentage*one_gram_calories
print(format(print_calories, ".4f"))