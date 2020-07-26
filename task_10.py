"""Рассчитаем сложный процент по кредиту

Нам нужны сведения:

Срок кредита в годах
Процентная ставка
Количество платежей в год
Сумма кредита

"""

period = 10
rate = .06
pay_counts = 12
credit_sum = 4000


def calc_1(credit_sum_val, pay_counts_val, period_val, rate_val):
    """Цикл"""
    total = period_val * pay_counts_val
    for _ in range(1, (total+1)):
        credit_sum_val = credit_sum_val*(1+(rate_val/pay_counts_val))
    return credit_sum_val


print(calc_1(credit_sum, pay_counts, period, rate))


def calc_2(credit_sum_val, pay_counts_val, period_val, rate_val, number_of_recursions):
    """Рекурсия"""
    if number_of_recursions == 0:
        total = pay_counts_val * period_val
    elif number_of_recursions != 0:
        total = period_val
    if period_val == 0:
        return credit_sum_val
    else:
        new_duration = total - 1
        amount = credit_sum_val*(1+(rate_val/pay_counts_val))
        return calc_2(amount, pay_counts_val, new_duration, rate_val, 1)


print(calc_2(credit_sum, pay_counts, period, rate, 0))


