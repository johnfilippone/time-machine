import sys
import time
import json


if __name__ == "__main__":
    record = {
        "date": time.strftime("%d/%m/%Y"),
        "minutes": sys.argv[1],
        "tags": sys.argv[2:]}
    
    with open("../data/records.pl", "a") as file:
        file.write(json.dumps(record) + "\n")
    
     
