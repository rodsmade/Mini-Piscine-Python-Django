import sys, antigravity

def validate_args():
    if len(sys.argv) != 4:
        print("Provide three arguments as follows:")
        print("\tpython3 geohashing.py [latitude] [longitude] [yyyy-mm-dd-Daw Jones opening points today]")
        print("E.g.:\tpython3 geohashing.py 37.421542 -122.085589 2005-05-26-10458.68")
        exit(-42)

    latitude = float(sys.argv[1])
    longitude = float(sys.argv[2])
    datedow = bytes(sys.argv[3], 'ascii')
    antigravity.geohash(latitude=latitude, longitude=longitude, datedow=datedow)

if __name__ == "__main__":
    validate_args()

