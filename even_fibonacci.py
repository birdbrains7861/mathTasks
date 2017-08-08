# FIND THE SUM OF ALL EVEN FIBONACCI NUMBERS NO GREATER THAN 4 MILLION


def fib_gen(f_previous, f_super_previous):

    return f_previous + f_super_previous

running_sum = 2

f_last = 1

f_current = 2

while f_current < 4 * 10**6:

    f_temp = f_current

    f_current = fib_gen(f_current, f_last)

    if f_current % 2 == 0:

        running_sum += f_current

    f_last = f_temp

print(running_sum)
