# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.
month = input('Enter the month of the year (Jan - Dec):')
season = ""
day = input('Enter the day of the month:')
month_day = 0
if (month == "Jan"):
    month_day = 1+ int(day)/100
elif (month == "Feb"):
    month_day = 2+ int(day)/100
elif (month == "Mar"):
    month_day = 3+ int(day)/100
elif (month == "Apr"):
    month_day = 4 + int(day)/100
elif (month == "May"):
    month_day = 5+ int(day)/100
elif (month == "Jun"):
    month_day = 6+ int(day)/100
elif (month == "Jul"):
    month_day = 7+ int(day)/100
elif (month == "Aug"):
    month_day = 8+ int(day)/100
elif (month == "Sep"):
    month_day = 9+ int(day)/100
elif (month == "Oct"):
    month_day = 10+ int(day)/100
elif (month == "Nov"):
    month_day = 11+ int(day)/100
elif (month == "Dec"):
    if (int(day) >= 21 and int(day) <= 31):
        season = "Winter"
    else: 
        season = "Fall"

if (month_day >= 1.01 and month_day <= 3.19):
    season = "Winter"
elif (month_day >= 3.20 and month_day <= 6.20):
    season = "Spring"
elif (month_day >= 6.21 and month_day <= 9.21):
    season = "Summer"
elif (month_day >= 9.22 and month_day <= 11.30):
    season = "Fall"
print(f'{month}. {day} is in {season}')
