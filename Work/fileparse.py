# fileparse.py
#
# Exercise 3.3

import csv

def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    '''
    Parse a CSV file into a list of records
    '''
    if select and not has_headers:
        raise RuntimeError('select atgument requires column headers')

    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)

        # Read the csv header
        if has_headers:
            headers = next(rows)

        if select:
            indices = [headers.index(colname) for colname in select ]
            headers = select
        else:
            indices = []
            
        records = []

        for rowno, row in enumerate(rows, start = 1):
            if not row:    #Skip row with no data
                continue
            if indices:
                row = [row[index] for index in indices]
            if types:
                try:   
                    converted = [ func(val) for func, val in zip(types, row) ]
                except ValueError as e:
                    if not silence_errors:
                        print(f'Row {rowno}: Couldn\'t convert {row}')
                        print(f'Row {rowno}: Reason {e}')

            if has_headers:
                record = dict(zip(headers, converted))
            else:
                record = tuple(converted)
            
            records.append(record)
    return records
