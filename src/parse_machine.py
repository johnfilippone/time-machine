#!/usr/bin/env python

import sys
import time
import json
import argparse
from record_parsers import get_records_by_date, generate_pichart_csv, generate_table_csv, record_reduce


def add_record(minutes, tag):
    """ 
    converts user input into a json record and appends it to the records file 
    
    inputs:
      args:  [ minutes:int, tag:String ]

    output:
      record: { date:String, minutes:int, tags:String[] }
    
    record is appeneded to records file
    """

    record = {
        "date": time.strftime("%d/%m/%Y"),
        "minutes": minutes,
        "tag": tag}

    with open("/home/filippone/repos/time-machine/data/records", "a") as f:
        f.write(json.dumps(record) + "\n")


def remove_last_record():
    """ removes the most recently added record from the records file """

    with open("/home/filippone/repos/time-machine/data/records", "r") as f:
        records = f.readlines()
    with open("/home/filippone/repos/time-machine/data/records", "w") as f:
        f.write("".join(records[:-1]))


def add_tag_assignment(child_tag, parent_tag):
    """ adds a tag assignment to the tag_assignments table """

    tag_assignment = {
        "child_tag": child_tag,
        "parent_tag": parent_tag}

    with open("/home/filippone/repos/time-machine/data/tag-assignments", "a") as f:
        f.write(json.dumps(tag_assignment) + "\n")



if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    directive_add = subparsers.add_parser("add")
    directive_add.set_defaults(command="add")
    directive_add.add_argument("minutes", type=int)
    directive_add.add_argument("tag")

    directive_revert = subparsers.add_parser("revert")
    directive_revert.set_defaults(command="revert")

    directive_assign = subparsers.add_parser("assign")
    directive_assign.set_defaults(command="assign")
    directive_assign.add_argument("child_tag")
    directive_assign.add_argument("parent_tag")

    args = parser.parse_args()
    
    if args.command == "add":
        add_record(args.minutes, args.tag)
    elif args.command == "revert":
        remove_last_record()
    elif args.command == "assign":
        add_tag_assignment(args.child_tag, args.parent_tag)


    # clear csv files
    open("/home/filippone/repos/time-machine/webapp/data/pichart.csv", "w").close()
    open("/home/filippone/repos/time-machine/webapp/data/table.csv", "w").close()

    # pull records
    with open("/home/filippone/repos/time-machine/data/records", "r") as f:
        records = f.readlines()

    # generate csv for webapp
    generate_pichart_csv(get_records_by_date(records, time.strftime("%d/%m/%Y")))
    generate_table_csv(get_records_by_date(records, time.strftime("%d/%m/%Y")))
    

    
 
        
    
    
     
