annual_salary = float(input('Enter your starting salary: '))

total_cost = 1000000.0
semi_annual_raise = 0.07
r = 0.04
portion_down_payment = 0.25*(total_cost)
current_savings = 0

low = 0
high = 10000
mid = (low + high) / 2.0
epsilon = 100.0
bisection_times = 0

while abs(current_savings - portion_down_payment) >= epsilon:
    current_savings = 0
    annual_salary_reset = annual_salary
    for month in range(1,37):
        current_savings += (current_savings * r + annual_salary_reset * mid /10000.0) / 12
        if month % 6 == 0:
            annual_salary_reset = annual_salary_reset * (1 + semi_annual_raise)

    if current_savings > portion_down_payment:
        high = mid
    else:
        low = mid
    mid = (high + low) / 2.0
    bisection_times += 1
    if bisection_times >= 15:
        break

if bisection_times < 15:
    print("Best savings rate: %0.4f" %(mid/10000.0))
    print("Step in bisection search: ", bisection_times)
else:
    print("It is not possible to pay the down payment in three years.")
	