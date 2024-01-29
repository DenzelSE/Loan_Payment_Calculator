def user_loan_data():
    print("#------Loan Details------#")
    principal = float(input(" 1. Enter the loan amount: "))
    interest_rate = float(input(" 2. Enter the annual interest rate (as a decimal): "))
    loan_term_years = int(input(" 3. Enter the loan term(in years): "))

    return principal, interest_rate, loan_term_years

def converting(principal,interest_rate,loan_term_years):
    #converting loan terms to months
    loan_term_months = loan_term_years *12
    
    #converting interest rate to monthly rate
    interest_rate_monthly = interest_rate / 12
    return loan_term_months, interest_rate_monthly

def calculations(principal,loan_term_months,interest_rate_monthly):

    monthly_payment = (principal *interest_rate_monthly)/(1-(1+interest_rate_monthly)**(-loan_term_months))

    total_amount_paid = monthly_payment * loan_term_months

    total_interest_paid = total_amount_paid - principal

    return monthly_payment, total_amount_paid, total_interest_paid

def results(monthly_payment, total_amount_paid, total_interest_paid, interest_rate,principal,loan_term_years):
    print("\n#------Loan Payment Calculations------#")
    print(" * Loan amount: R{:,.2f}".format(principal))
    print(" * Interest rate: {:.2%}".format(interest_rate))
    print(" * Loan term: {} years".format(loan_term_years))
    print(" * Monthly payment: R{:,.2f}".format(monthly_payment))
    print(" * Total amount paid: R{:,.2f}".format(total_amount_paid))
    print(" * Total interest paid: R{:,.2f}".format(total_interest_paid))

def main():
    principal,interest_rate, loan_term_years = user_loan_data()
    loan_term_months, interest_rate_monthly = converting(principal,interest_rate,loan_term_years)
    monthly_payment, total_amount_paid, total_interest_paid = calculations(principal,loan_term_months,interest_rate_monthly)
    results(monthly_payment,total_amount_paid,total_interest_paid, interest_rate,principal,loan_term_years)

if __name__ == '__main__':
    main()