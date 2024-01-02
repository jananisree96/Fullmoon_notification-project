import ephem

def calculate_next_full_moon():
    next_full_moon = ephem.next_full_moon(ephem.now())
    return next_full_moon

next_full_moon_date = calculate_next_full_moon()
print("The next full moon is on", next_full_moon_date)
