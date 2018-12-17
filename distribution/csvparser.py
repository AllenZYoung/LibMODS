import csv
from collections import namedtuple
from pprint import pprint
CSVFILE = '../2018-MidYearCommunityPartnershipPosters-PC-PM-LIC - Metadata.csv'

def parse_row(row):
  Record = namedtuple('Record', ['Author','Title','Keywords'])
  r = None
  try:
    r = Record(row[0],row[1],row[2])
  except IndexError:
    print('illegal row here,\t{}'.format(row))
  return r

def open_csv():
  result = []
  linenumber = 0
  with open(CSVFILE) as f:
    reader = csv.reader(f)
    for row in reader:
      if linenumber == 0:
        pass
      else:
        result.append(parse_row(row))
      linenumber += 1
  pprint(result)
  return result

def get_records():
  return open_csv()



if __name__ == '__main__':
  open_csv()