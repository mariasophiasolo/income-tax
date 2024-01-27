# calculating income tax

def calculate_income_tax(income):
    tax_payable = 0
    # if the income is less than or equal to 10000
    if income <= 10000:
        tax_payable = 0

    # else if the income is less than or equal to 20000
    elif income <= 20000:
        x = income - 10000

        # then apply the 10% tax on the remainiing income
        tax_payable = x * 10 / 100

    else:
        # calculate the tax for the first 10000
        tax_payable = 0

        # apply again the 10% tax on the next 10000
        tax_payable += 10000 * 10 / 100

        # apply the 20% tax on the remaining income
        tax_payable += (income - 20000) * 20 / 100

    return tax_payable
