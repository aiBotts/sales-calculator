# This program calculates statics for quarterly sales

quarterly_sum = []  # Create an empty list


# Defining the main function
def main():
    print()
    # Calling each function appropriately
    display()
    print()
    get_quarterly_sales()
    print()
    process_sales()


# Define a function for the display header of the program
def display():
    print('The Quarterly Sales program')


# Defining the get quarterly sales function
def get_quarterly_sales():
    # Creating each variable for the user
    q1 = float(input('Enter the sales for Q1: '))
    q2 = float(input('Enter the sales for Q2: '))
    q3 = float(input('Enter the sales for Q3: '))
    q4 = float(input('Enter the sales for Q4: '))

    quarterly_sum.append(q1)  # appending q1 back to the list
    quarterly_sum.append(q2)  # appending q2 back to the list
    quarterly_sum.append(q3)  # appending q3 back to the list
    quarterly_sum.append(q4)  # appending q4 back to the list

    return quarterly_sum  # returning the list so i can use it in other functions


# Defining the process sales function
def process_sales():
    # Creating a total variable to calculate total sales entered each quarter
    total = sum(quarterly_sum)
    average = total / len(quarterly_sum)  # Creating the average variable to average each quarter of sales
    lowest = min(quarterly_sum)  # Creating the lowest variable to find lowest sales
    highest = max(quarterly_sum)  # Creating the highest variable to find the highest sales

    t = "{:,.2f}".format(total)  # Formatting for commas :)
    a = "{:,.2f}".format(average)
    lo = "{:,.2f}".format(lowest)
    h = "{:,.2f}".format(highest)

    print('Total: $', t)  # Printing the Total sum of each quarter
    print('Average Quarter: $', a)  # Calculating the average between all q's
    print('Lowest Quarter: $', lo)  # Printing the lowest quarter
    print('Highest Quarter: $', h)  # Printing the highest quarter


# Calling the main function
main()
