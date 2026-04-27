from cs50 import get_float

# user fails to provide a non-negative value, your program should re-prompt the user for a valid amount again and again until the user complies
# as c as capital as video
while True:
    dollars = get_float("Change: ")  # not change its dollars so
    if dollars >= 0:
        break  # other wise break
# as question assume that the only coins available are quarters (25¢), dimes (10¢), nickels (5¢), and pennies (1¢)...p


# to convert dollars to cent using round like nearest interget that question wants like 3.5 = 4  123.45 = 120 nearest to ten ... and * 100 to convert 0.41 to 40

cents = round(dollars * 100)  # user input * 100
# instalize the counter of coins like it start from zero
coins = 0

# as question to calculate quarters (25 cents)
while cents >= 25:  # only count this and add one coin if found other wise go to dimes or 10 cents
    cents -= 25  # like explained in operators in c formula += is x +=5 which is x = x + 5 means user value + 5 so here cents in thens like 40 -25 again after counting 1 coins it again go to dimes as >= 10 and two
    coins += 1  # count one if it is done

# to calculate dimes (10 cents) # like same situation easy than in c
while cents >= 10:
    cents -= 10
    coins += 1

# to calculate nickels (5 cents)
while cents >= 5:
    cents -= 5
    coins += 1


# to calculate pennies (1 cents)
while cents >= 1:
    cents -= 1
    coins += 1

print(coins)  # like total numbers of coins used to make change final result after all ..
