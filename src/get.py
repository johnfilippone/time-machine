import sys
import time
import json


if __name__ == "__main__":
    
    with open("../data/records.pl", "r") as file:
        a = file.readlines()
        print json.loads(a[0])

    
     
