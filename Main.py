
import time

while True:
    starting_capital = int(input("Starting Capital(first month): "))
    regular_investment = int(input("Regular Investment(monthly): "))
    interest_rate = int(input("APY(% yearly return rate)"))
    total_investment_period = int(input("Total Investment Period(months): "))

    def get_current_daily_interest(total_investment):
        return (total_investment * (interest_rate/100)) /365

    accrued_interest = 0
    total_interest_dict = {}
    total_capital_dict = {}
    total_capital = starting_capital
    total_interest_dict[1] = get_current_daily_interest(total_capital) * 30
    total_capital_dict[1] = [total_capital,accrued_interest]
    accrued_interest += total_interest_dict[1]
    for i in range(2,(total_investment_period+1)):
        total_capital += regular_investment
        
        total_interest_dict[i] = get_current_daily_interest(total_capital + accrued_interest) * 30
        accrued_interest += total_interest_dict[i]
        total_capital_dict[i] = [total_capital, accrued_interest]

    for key in total_interest_dict.keys():
        print(f"[Month: {key}---Total Investment(Out Of Pocket): ${total_capital_dict[key][0]}---Total Investment(Plus Interest): ${str(round(total_capital_dict[key][1] + total_capital_dict[key][0],2))}---Monthly Interest: ${round(total_interest_dict[key],2)}]")

    print(f"Total Capital: ${round(total_capital+accrued_interest,2)}")
    time.sleep(5)
