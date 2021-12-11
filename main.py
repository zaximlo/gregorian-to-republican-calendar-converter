import datetime

def bissextile(year):
    return (year%4 == 0 and year%100 != 0)

def intput(x, n_max=None, n_min = None):
    return int(input(x))



Months = ['Vendemiaire', 'Brumaire', 'Frimaire',
      'Nivose', 'Pluviose', 'Ventose',
      'Germinal', 'Floreal', 'Prairial',
      'Messidor', 'Thermidor', 'Fructidor',
      'sans-culottides']

reference = datetime.date(1792, 9, 22) #1 Vendemiaire 1

to_day = datetime.date(intput('y: '),
                     intput('m: '),
                     intput('d: '))

year = day = month = 1

while reference != to_day:
    if month == 13:
        if bissextile(year):
            if day < 6:
                day += 1
            elif day == 6:
                day = month = 1
                year += 1
        else:
            if day == 5:
                day = month = 1
                year += 1
            else:
                day += 1
    else:
        if day == 30:
            day = 1
            month += 1
        else:
            day += 1
    reference = reference + datetime.timedelta(days = 1)

#feedback
input(f'''
This corresponds to / Ceci correspond au {day} {Months[month-1]} {year} --> {day}/{month}/{year}''')