Base_hours = 40
OT_Multiplier = 1.5
hours = float(input("Enter the number of hours worked:"))
pay_rate = float(input("Enter the hourly pay rate: "))
if hours>Base_hours :
    overtime = hours - Base_hours
    Overtime_pay = overtime_hours * pay_rate * OT_Multiplier
    gross_pay = Base_hours * pay_rate + Overtime_pay
else:
        gross_pay = hours * pay_rate
        print(f"The gross pay is ${gross_pay:,.2f}.")
