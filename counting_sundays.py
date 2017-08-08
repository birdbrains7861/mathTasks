# GIVEN THAT 1 JAN 1900 IS A MONDAY, FIND THE NUMBER OF SUNDAYS WHICH FALL ON THE FIRST
# OF THE MONTH IN THE 20TH CENTURY (1 JAN 1901 - 31 DEC 2000)

sunday_count = 0

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

shift = 0

for year in range(1900, 2001):

    if year % 4 == 0 and year != 1900:

        months[1] = 29

    for month in months:

        for day in range(1, month+1):

            root = ((day+shift+1) % 7) - 1

            if root == -1:

                root = 6

            if year != 1900 and day == 1 and days[root] == "Sunday":

                sunday_count += 1

            if day == month:

                shift = root

    months[1] = 28

print(sunday_count)