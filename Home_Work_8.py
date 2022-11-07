from datetime import datetime, date, timedelta

def get_birthdays_per_week(users:list) -> None:
    timetable = {"Monday": [],
                "Tuesday": [],
                "Wednesday": [],
                "Thursday": [],
                "Friday": [],
                "Next Monday": []
    }
    delta = timedelta(days=7)
    delta_date = datetime.now() + delta
    for dict_worker in users:
        birthday_date = datetime(year=datetime.now().year, month=dict_worker.get('birthday').month, day=dict_worker.get('birthday').day)
        birthday_date_next_year = datetime(year=datetime.now().year + 1, month=dict_worker.get('birthday').month, day=dict_worker.get('birthday').day)
        
        if datetime.now() < birthday_date <= delta_date or datetime.now() < birthday_date_next_year <= delta_date:
            if datetime.now() < birthday_date_next_year <= delta_date:
                birthday_date = birthday_date_next_year
            if datetime.now().weekday() < 5:
                if birthday_date.weekday() < 5:
                    wd_list = timetable.get(birthday_date.strftime('%A'))
                    wd_list.append(dict_worker.get('name'))
                    timetable[birthday_date.strftime('%A')] = wd_list
                else:
                    wd_list = timetable.get("Monday")
                    wd_list.append(dict_worker.get('name'))
                    timetable["Monday"] = wd_list
            elif datetime.now().weekday() == 5:
                if birthday_date.weekday() < 5:
                    wd_list = timetable.get(birthday_date.strftime('%A'))
                    wd_list.append(dict_worker.get('name'))
                    timetable[birthday_date.strftime('%A')] = wd_list
                elif birthday_date.weekday() == 5:
                    wd_list = timetable.get("Monday")
                    wd_list.append(dict_worker.get('name'))
                    timetable["Monday"] = wd_list
                else:
                    wd_list = timetable.get("Next Monday")
                    wd_list.append(dict_worker.get('name'))
                    timetable["Next Monday"] = wd_list
            else:
                if birthday_date.weekday() < 5:
                    wd_list = timetable.get(birthday_date.strftime('%A'))
                    wd_list.append(dict_worker.get('name'))
                    timetable[birthday_date.strftime('%A')] = wd_list
                else:
                    wd_list = timetable.get("Next Monday")
                    wd_list.append(dict_worker.get('name'))
                    timetable["Next Monday"] = wd_list
    for key, value in timetable.items():
        if len(value) > 0:
            print(f'{key}: {", ".join(value)}')
