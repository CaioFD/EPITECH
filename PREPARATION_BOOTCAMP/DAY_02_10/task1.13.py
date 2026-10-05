def ship(*names, **address):
    print(*names)
    for key, value in address.items():
        print(f"{key}: {value}")


ship("Batman", street="Mountain Drive", city="Gotham")
ship("Superman", "The man of steel", apartment="3D", num=344,
     street="Clinton Street", city="Metropolis")