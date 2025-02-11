date_str = "01-JUN-2021"
day, month_str, year = date_str.split('-')
month_mapping = {
  "JAN": 1, "FEB": 2, "MAR": 3, "APR": 4, "MAY": 5, "JUN": 6,
    "JUL": 7, "AUG": 8, "SEP": 9, "OCT": 10, "NOV": 11, "DEC": 12
}
month_num = month_mapping[month_str.upper()]
print(f"Original Date: {date_str}")
print(f"Day: {day}")
print(f"Month: {month_str}")
print(f"Year: {year}")
print(f"Numerical Value of the Month: {month_num}")
