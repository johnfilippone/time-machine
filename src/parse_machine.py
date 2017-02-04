import sys
import time
import json


def add_record(args):

    record = {
        "date": time.strftime("%d/%m/%Y"),
        "minutes": sys.argv[0],
        "tags": sys.argv[1:]}

    with open("../data/records.pl", "a") as f:
        f.write(json.dumps(record) + "\n")




if __name__ == "__main__":
    if sys.argv[1] == "-c":
        with open("../data/records.pl", "r") as f:
            lines = f.readlines()

        with open("/var/www/html/time-machine.csv", "w") as f:
            f.write("tag,population\n")
        with open("/var/www/html/time-machine.csv", "a") as f:
            for line in lines:
                record = json.loads(line)
                f.write(str(record["tags"][0]) + "," + str(record["minutes"]) + "\n")
    else:
        add_record(sys.argv[1:])
     
        
    
    
     
