def format_exp(years, months):
    if years % 10 == 1 and years % 100 != 11:
        year_word = "год"
    elif years % 10 in [2, 3, 4] and not (years % 100 in [12, 13, 14]):
        year_word = "года"
    else:
        year_word = "лет"
    if months % 10 == 1 and months % 100 != 11:
        month_word = "месяц"
    elif months % 10 in [2, 3, 4] and not (months % 100 in [12, 13, 14]):
        month_word = "месяца"
    else:
        month_word = "месяцев"
    experience_str = f"{years} {year_word} и {months} {month_word}"
    return experience_str


def calculate_exp(start, end):
    delta = end - start
    years = delta.days // 365
    remaining_days = delta.days % 365
    months = remaining_days // 30
    return format_exp(years, months)


def get_exp(start, end):
    return calculate_exp(start, end)
