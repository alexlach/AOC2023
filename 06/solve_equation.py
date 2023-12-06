from sympy import symbols, Eq, solve

# Define the variables
time_hold, total_time = symbols('time_hold total_time')
distance = symbols('distance')

# Define the equation
equation = Eq(distance, time_hold * (total_time - time_hold))

# Solve the equation for time_hold
solutions = solve(equation, time_hold)
print(solutions)

# total_time/2 - sqrt(-4*distance + total_time**2)/2
# total_time/2 + sqrt(-4*distance + total_time**2)/2