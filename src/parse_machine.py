import sys
import time
import json


def add_record(args):
    """ takes user input and turns it into a json record in the records.pl file """

    record = {
        "date": time.strftime("%d/%m/%Y"),
        "minutes": args[0],
        "tags": args[1:]}

    with open("../data/records.pl", "a") as f:
        f.write(json.dumps(record) + "\n")

def get_todays_records(records):
    """ returns the set of the records that were recorded today """

    todays_records = []

    for line in records:
        record = json.loads(line) 
        if record["date"] == time.strftime("%d/%m/%Y"):
            todays_records.append(line)
    return todays_records

def generate_csv(records):
    """ pulls records from file and turns them into a csv file that D3.js can understand """

    # add csv table headers
    with open("/var/www/html/time-machine.csv", "w") as f:
        f.write("tag,population\n")

    # aggregate similar tags
    valid_tags = set([" - ".join(json.loads(record)["tags"]) for record in records])
    aggregated_records = record_reduce(records, valid_tags)

    # write each entry in the aggregated_records dict to a row in the csv table
    with open("/var/www/html/time-machine.csv", "a") as f:
        for tag, minutes in aggregated_records.iteritems():
            f.write(str(tag) + "," + str(minutes) + "\n")

def record_reduce(records, valid_tags):
    """ 
    inputs: array of records in json string format
    output: dict that maps tags to total minutes

    combines similar tags
    """
    aggregated_records = {tag:0 for tag in valid_tags}
    for line in records:
        record = json.loads(line) 
        aggregated_records[" - ".join(record["tags"])] += int(record["minutes"])
    
    # add grey time: time not logged today
    aggregated_records["grey-time"] = 1440 - sum(time_used for time_used in aggregated_records.values())
    return aggregated_records


if __name__ == "__main__":

    add_record(sys.argv[1:])

    # pull records and generate csv for D3.js pi chart
    with open("../data/records.pl", "r") as f:
        records = f.readlines()

    generate_csv(get_todays_records(records))

    
 
        
    
    
     
