name = input('Enter your name: ')
flg_error_salary = True
flg_error_bonus = True

while flg_error_salary:
    try:
        salary = float(input('Enter your salary: ').replace(',', '.'))
    except ValueError:
        print('Invalid input. Please enter numbers only.')
    else:
        flg_error_salary = False

while flg_error_bonus:
    try:
        bonus_percentage = float(input('Enter the bonus percentage: ').replace(',', '.'))
    except ValueError:
        print('Invalid input. Please enter numbers only.')
    else:
        flg_error_bonus = False

final_bonus = salary * bonus_percentage
print(f'Hello {name}! Your bonus is: {final_bonus}')
