import sys
import time

sys.path.append("../../src")
from record_parsers import generate_pichart_csv, generate_table_csv


# clear csv files
open("/home/filippone/repos/time-machine/webapp/data/pichart.csv", "w").close()
open("/home/filippone/repos/time-machine/webapp/data/table.csv", "w").close()

# pull records
with open("/home/filippone/repos/time-machine/data/records", "r") as f:
    records = f.readlines()

# generate csv for webapp
generate_pichart_csv(get_records_by_date(records, time.strftime("%d/%m/%Y")))
generate_table_csv(get_records_by_date(records, time.strftime("%d/%m/%Y")))

