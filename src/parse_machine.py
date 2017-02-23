#!/usr/bin/env python

import sys
import time
import json
from record_parsers import get_records_by_date, generate_pichart_csv, generate_table_csv, record_reduce


def add_record(minutes, tag):
    """ 
    takes user input and turns it into a json record in the records file 
    
    inputs:
      args:  [ minutes:int, tags:String[] ]

    output to file:
      record: { date:String, minutes:int, tags:String[] }
    """

    record = {
        "date": time.strftime("%d/%m/%Y"),
        "minutes": minutes,
        "tag": tag}

    with open("/home/filippone/repos/time-machine/data/records", "a") as f:
        f.write(json.dumps(record) + "\n")



if __name__ == "__main__":

    
    add_record(sys.argv[1], sys.argv[2])

    # clear csv files
    open("/home/filippone/repos/time-machine/webapp/data/pichart.csv", "w").close()
    open("/home/filippone/repos/time-machine/webapp/data/table.csv", "w").close()

    # pull records
    with open("/home/filippone/repos/time-machine/data/records", "r") as f:
        records = f.readlines()

    # generate csv for webapp
    generate_pichart_csv(get_records_by_date(records, time.strftime("%d/%m/%Y")))
    generate_table_csv(get_records_by_date(records, time.strftime("%d/%m/%Y")))
    

    
 
        
    
    
     
