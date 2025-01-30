"""
PRIMM: Python Data Processing
In this PRIMM Activity, you'll learn how to process a 
CSV file and complete some basic extraction techniques.

Joshua Schreyer - January 2025
"""

import csv
from typing import Union

def convert_record_data(record: dict[str, Union[str, int]]) -> None:
  record["OBJECTID"] = int(record["OBJECTID"])
  record["REPORTYEAR"] = int(record["REPORTYEAR"])
  record["ReportNumber"] = int(record["ReportNumber"])
  record["PropValue"] = float(record["PropValue"])
  if record["Serial"] == "Yes":
    record["Serial"] = True
  else:
    record["Serial"] = False
  if record["x"] != None:
    record["x"] = float(record["x"])
  if record["y"] != None:
    record["y"] = float(record["y"])
  return record

def get_records(data_filename: str) -> list[dict[str, Union[str, int]]]:
  """
  Gets records from a csv data file.
  Parameters:
    data_filename(str): The location and name of the csv file that contains the data
  Returns:
    list[dict[str, Union[int, str]]]: a list of records where each 
        record is a dictionary where the keys are strings 
        and the values can be int or str
  """
  records: list[dict[str,Union[str, int]]] = []
  with open(data_filename, "r", encoding='utf-8-sig') as data_file:
    reader: csv.DictReader = csv.DictReader(data_file)
    for record in reader:      
      records.append(record)

  return records

def most_bikes_stolen(records):
  counts = {}
  for item in records:
    if item["District"] in counts:
      counts[item["District"]] += 1
    else:
      counts[item["District"]] = 1
  sorted_by_values = dict(sorted(counts.items(), key=lambda item: item[1]))
  return list(sorted_by_values)[-1]

def main() -> None:
  data_filename: str = "resources/stolen_bikes.csv"
  records: list[dict[str, Union[str, int]]] = get_records(data_filename)
  converted_records = []

  for record in records:
    converted_records.append(convert_record_data(record))

  print(f"{len(records)} records read in.")

  print("District with most bikes stolen: " + most_bikes_stolen(converted_records))


if __name__ == "__main__":
  main()