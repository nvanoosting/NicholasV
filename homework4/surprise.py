# File: surprise.py

# Below is a dictionary of targets you want to observe.

# If you are an observational astronomer or instrumentalist, picking the correct targets
# to point the telescope at is very important. Let's practice below.

targets = {
    "Vega": {
        "RA": "18h 36m 56.3s",
        "Dec": "+38° 47′ 01″",
        "Magnitude": 0.03,
        "Spectral Type": "A0Va"
    },
    "Betelgeuse": {
        "RA": "05h 55m 10.3s",
        "Dec": "+07° 24′ 25″",
        "Magnitude": 0.42,
        "Spectral Type": "M1-M2 Ia-Ib"
    },
    "Sirius": {
        "RA": "06h 45m 08.9s",
        "Dec": "-16° 42′ 58″",
        "Magnitude": -1.46,
        "Spectral Type": "A1V"
    },
    "Rigel": {
        "RA": "05h 14m 32.3s",
        "Dec": "-08° 12′ 06″",
        "Magnitude": 0.12,
        "Spectral Type": "B8Ia"
    },
    "Polaris": {
        "RA": "02h 31m 49.1s",
        "Dec": "+89° 15′ 51″",
        "Magnitude": 1.97,
        "Spectral Type": "F7Ib"
    }
}

# --- Questions ---
# 1) Write a function that uses a loop to print the name of each star.
# 2) Write a function that uses a loop to print the name of each star with its spectral type.
# 3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.
# 4) Look up another target, add all the necessary information to the targets list. 
# 5) Write a function that finds the brightest star whose Declination is closest to 20°.
# 6) What is your favorite constellation?

def star_names(stars):
    for star in stars: # iterates over the entire dictionary 
        print(star) # prints every key

def star_name_type(stars):
    for star in stars: # iterates over the entire dictionary
        print(star, ":", stars[star]["Spectral Type"]) # prints the star name and the spectral type

def star_magnitude_comparison(stars):
    list_magnitude_greater_than_value = {}
    for star in stars:
        if stars[star]["Magnitude"] > 0.1:
            list_magnitude_greater_than_value[star] = stars[star]["Magnitude"]
    return list_magnitude_greater_than_value

targets["Proxima Centauri"] = {"RA" : "14h  29m 43s", "Dec" : "-62° 40' 36″", "Magnitude" : 15.5, "Spectral Type" : "M5.5Ve"}

def star_closest_to_20_degrees_func(stars):
    name_closest_to_20_degrees = 0
    value_closest_to_20_degrees = 0
    for star in stars:
        if abs(20 - int(stars[star]["Dec"][0:3])) < abs(20 - int(value_closest_to_20_degrees)):
            name_closest_to_20_degrees = star
            value_closest_to_20_degrees = stars[star]["Dec"][0:3]
    return f"{name_closest_to_20_degrees} : {value_closest_to_20_degrees}°"

print("My favorite constellation is Ursa Major")
