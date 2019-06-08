# Nested if else

isInternetConnected = True
isGPSConnected = False

if isInternetConnected:
    print("You can browse Google Maps")
    if isGPSConnected:
        print("You can Navigate using Google Maps")
    else:
        print("To use Navigation using Google Maps enable GPS")
else:
    print("Please connect to internet")
