import time
import json

def get_records_by_date(records, date):
    """ returns the set of the records that were recorded today """

    todays_records = []

    for line in records:
        record = json.loads(line)
        if record["date"] == date:
            todays_records.append(line)
    return todays_records


def generate_pichart_csv(records):
    """ pulls records from file and turns them into a csv file that D3.js can understand """

    # aggregate similar tags
    valid_tags = set([" - ".join(json.loads(record)["tags"]) for record in records])
    aggregated_records = record_reduce(records, valid_tags)

    # write each entry in the aggregated_records dict to a row in the csv table
    with open("/home/filippone/repos/time-machine/webapp/data/pichart.csv", "a") as f:
        rows = ["tag,population"]
        #f.write("tag,population\n")
        for tag, minutes in aggregated_records.iteritems():
            rows.append(str(tag) + "," + str(minutes))
        f.write("\n".join(rows))


def generate_table_csv(records):
    """ pulls records from file and turns them into a csv file that D3.js can understand """

    # aggregate similar tags
    valid_tags = set([" - ".join(json.loads(record)["tags"]) for record in records])
    aggregated_records = record_reduce(records, valid_tags)

    # write each entry in the aggregated_records dict to a row in the csv table
    with open("/home/filippone/repos/time-machine/webapp/data/table.csv", "a") as f:
        rows = ["#,Activity,Minutes"]
        rank = 1
        for tag, minutes in sorted(aggregated_records.items(), key=lambda x: x[1], reverse=True):
            rows.append(str(rank) + "," + str(tag) + "," + str(minutes))
            rank += 1
        f.write("\n".join(rows))


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

