import csv
from collections import namedtuple
from pprint import pprint
CSVFILE = 'Posters.csv'

category_map_dict = {
  'Poster': ['Author', 'Title', 'Keywords'],
}

def get_category_by_filename(filename):
  if filename.startswith('Posters'):
    return 'Poster'

def parse_row(row, category):
  fields = category_map_dict[category]
  Record = namedtuple('Record', fields)
  r = None
  try:
    print([one for one in row])
    r = Record(*[one for one in row])
  except IndexError:
    print('illegal row here,\t{}'.format(row))
  return r

def open_csv(filename=None):
  if filename is None:
    filename = CSVFILE
  category = get_category_by_filename(filename)
  result = []
  linenumber = 0
  with open(filename) as f:
    reader = csv.reader(f)
    for row in reader:
      if linenumber == 0:
        pass
      else:
        result.append(parse_row(row, category))
      linenumber += 1
  pprint(result)
  return result, category

def get_records():
  return open_csv()



if __name__ == '__main__':
  open_csv()