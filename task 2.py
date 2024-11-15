def convert_seconds(seconds):
    days = seconds // 86400
    seconds = seconds % 86400
    hours = seconds // 3600
    seconds = seconds % 3600
    minutes = seconds // 60
    seconds = seconds % 60
    return f"{days}:{hours:02}:{minutes:02}:{seconds:02}"
total_seconds = int(input("Enter the number of seconds: "))
print("Time in days:", convert_seconds(total_seconds))
