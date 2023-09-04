from datetime import date, datetime, timedelta

weekdays=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Sunday", "Saturday"]

def get_next_week_dates():
    this_week={}
    dt = date.today()
    for i in range(7):
        result = dt + timedelta(days=i)
        dt_chged = result.strftime('%Y-%m-%d')
        this_week[("-".join(dt_chged.split("-")[1:]))]=(weekdays[result.weekday()])
    return this_week


def get_birthdays_per_week(users):
    print(users)
    rslt={}
    this_week=get_next_week_dates()
    for user in users: 
        name = user["name"].split()[0]
        raw_bd = user["birthday"].strftime('%Y-%m-%d')
        bd = "-".join(raw_bd.split("-")[1:])
        for date,day in this_week.items():
            if date==bd:
                if day in rslt:
                    if day in ['Sunday', 'Saturday']:
                        rslt['Monday'].append(name)
                    else:
                        rslt[day].append(name)
                else:
                    if day in ['Sunday', 'Saturday']:
                        rslt['Monday']= [name]
                    else:
                        rslt[day]=[name]
    users = rslt
    return users


if __name__ == "__main__":
    users = [{"name": "Bill Gates", "birthday": datetime(1955, 10, 28).date()}
         ]
    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
