'''
Exercise 12: Calculate income tax for the given income by adhering to the rules below
Taxable Income	Rate (in %)
First $10,000	0
Next $10,000	10
The remaining	20
Expected Output:

For example, suppose the taxable income is 45000, and the income tax payable is

10000*0% + 10000*10%  + 25000*20% = $6000.

'''


#Solution 1

total_income = int(input("Inter Your total income: "))

def TaxableIncome(total_income):

    new_total_income = 0
    total_income_taxable = 0

    if total_income >= 10000:
        new_total_income = total_income - 10000
    
        if new_total_income >= 10000:
            total_income_taxable = total_income_taxable + ((10000 * 10) / 100)
            new_total_income = new_total_income - 10000

            if new_total_income >= 1:
                total_income_taxable = total_income_taxable + ((new_total_income * 20) / 100)
                print("total_income_taxable", total_income_taxable)
            
            else:
                print("total_income_taxable", total_income_taxable)

        else:
            print("total_income_taxable", total_income_taxable)

    else:
        print("total_income_taxable", total_income_taxable)


TaxableIncome(total_income)