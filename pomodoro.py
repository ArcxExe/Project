def current_time(stop_time=0):
    current_datetime = datetime.now()
    current_hour = current_datetime.hour
    current_minute = current_datetime.minute
    if stop_time == 0:
        print(f"Текущее время: {current_hour}:{current_minute:02}")
    else:
        stop_minute = stop_time % 60
        stop_hour = stop_time // 60
        if current_minute + stop_minute >= 60:
            end_time_minute = (current_minute + stop_minute) % 60
            return f"Мы Закончим: {current_hour+stop_hour+1}:{end_time_minute:02}"
        return f"Мы закончим: {current_hour+stop_hour}:{current_minute+stop_minute:02}"

