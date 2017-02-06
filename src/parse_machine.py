#!/usr/bin/env python

import sys
import time
import json
from record_parsers import get_todays_records, generate_pichart_csv, generate_table_csv, record_reduce


def add_record(args):
    """ 
    takes user input and turns it into a json record in the records.pl file 
    
    inputs:
      args:  [ minutes:int, tags:String[] ]

    output to file:
      record: { date:String, minutes:int, tags:String[] }
    """

    record = {
        "date": time.strftime("%d/%m/%Y"),
        "minutes": args[0],
        "tags": args[1:]}

    with open("/home/filippone/repos/time-machine/data/records.pl", "a") as f:
        f.write(json.dumps(record) + "\n")



if __name__ == "__main__":

    
    add_record(sys.argv[1:])

    # clear csv files
    open("/home/filippone/repos/time-machine/webapp/data/time-machine.csv", "w").close()
    open("/home/filippone/repos/time-machine/webapp/data/table.csv", "w").close()

    # pull records
    with open("/home/filippone/repos/time-machine/data/records.pl", "r") as f:
        records = f.readlines()

    # generate csv for webapp
    generate_pichart_csv(get_todays_records(records))
    generate_table_csv(get_todays_records(records))
    

    
 
        
    
    
     
