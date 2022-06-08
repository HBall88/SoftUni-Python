def grades(grade):
    if 2.00<=grade<=2.99:
        print("Fail")
    elif 3.00<=grade<=3.49:
        print(f'Poor')
    elif 3.50<=grade<=4.49:
        print(f'Good')
    elif 4.50<=grade<=5.49:
        print(f'Very Good')
    elif 5.50<=grade<=6.00:
        print(f'Excellent')

grades(float(input()))