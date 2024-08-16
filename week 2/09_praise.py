praise ="good!"
lot_of_praise = praise * 4
print(praise)
print(lot_of_praise)

def get_minutes(hours, minutes):
    total = hours * 60 + minutes
    return total

# hours = float(input("Enter hours:"))
# minutes = float(input("Enter minutes:"))
# total_minutes = get_minutes(hours,minutes)
# print(total_minutes,"minutes")

total_minutes = get_minutes(3,44)
print(get_minutes(5,0),"minutes")
print(get_minutes(11,540),"minutes")


