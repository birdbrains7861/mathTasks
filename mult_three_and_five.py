# FIND THE SUM OF ALL NATURAL MULTIPLES OF 3 OR 5 WHICH LESS THAN 1000

count = 0

for n in range(1, 1000):

    mod_3 = n % 3

    mod_5 = n % 5

    if mod_3 == 0 or mod_5 == 0:

        count += n

print(count)
