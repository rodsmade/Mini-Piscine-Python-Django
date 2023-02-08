import sys, antigravity

def validate_args():
    if len(sys.argv) != 4:
        print("Provide three arguments as follows:")
        print("\tpython3 geohashing.py [latitude] [longitude] [yyyy-mm-dd-Daw Jones opening points today]")
        print("E.g.:\tpython3 geohashing.py 37.421542 -122.085589 2005-05-26-10458.68")
        exit(-42)

    try:
        latitude = float(sys.argv[1])
        longitude = float(sys.argv[2])
    except ValueError:
        sys.exit("Wrong format for latitude/longitude. Fix yo' shi'!")
     
    if abs(latitude) > 90.0:
         exit("Latitude out of range! Must be between -90 and +90")
    if abs(longitude) > 180.0:
         exit("Longitude out of range! Must be between -180 and +180")
    datedow = bytes(sys.argv[3], 'ascii')
    antigravity.geohash(latitude=latitude, longitude=longitude, datedow=datedow)

if __name__ == "__main__":
    validate_args()

