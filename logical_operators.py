high_income = True
high_credit = True
has_criminal_record = False
# If a person has high income and high credit, he is eligible for loan

if high_credit and high_income:
    print ("Eligible for Loan")

# If a person has high income or high credit, he is eligible for loan
if high_credit or high_income:
    print ("Eligible for Loan")

# If a person has high credit and no criminal record, he is eligible for loan
if high_credit and not has_criminal_record:
    print ("Eligible for Loan also")