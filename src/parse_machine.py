import sys
import time
import json


def add_record(args):

    record = {
        "date": time.strftime("%d/%m/%Y"),
        "minutes": args[0],
        "tags": args[1:]}

    with open("../data/records.pl", "a") as f:
        f.write(json.dumps(record) + "\n")


def generate_csv():
    with open("../data/records.pl", "r") as f:
        lines = f.readlines()

    with open("/var/www/html/time-machine.csv", "w") as f:
        f.write("tag,population\n")
    with open("/var/www/html/time-machine.csv", "a") as f:
        for line in lines:
            record = json.loads(line)
            f.write(str(record["tags"][0]) + "," + str(record["minutes"]) + "\n")



if __name__ == "__main__":

    add_record(sys.argv[1:])
    generate_csv()

    
 
        
    
    
     
