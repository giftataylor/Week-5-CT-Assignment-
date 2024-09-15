# Part 1: Average Rainfall Calculation

# Ask the user for the number of years
years = int(input("Enter the number of years: "))

# Initialize total rainfall and month counter
total_rainfall = 0
total_months = 0

# Outer loop for each year
for year in range(1, years + 1):
    print(f"\nYear {year}:")
    
    # Inner loop for each month (12 months)
    for month in range(1, 13):
        rainfall = float(input(f"Enter the rainfall (in inches) for month {month}: "))
        total_rainfall += rainfall
        total_months += 1

# Calculate the average rainfall
average_rainfall = total_rainfall / total_months

# Display the results
print(f"\nTotal number of months: {total_months}")
print(f"Total inches of rainfall: {total_rainfall:.2f}")
print(f"Average rainfall per month: {average_rainfall:.2f} inches")
