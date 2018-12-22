from bs4 import BeautifulSoup
from pprint import pprint

SAMPLE_FILE = 'sample.xml'
OUTPUT_FILE = '../output/Poster-{}.xml'
from csvparser import *


def output_one(record, category):
  xml = None
  with open(SAMPLE_FILE) as f:
    xml = BeautifulSoup(f,'xml')
    print(xml)

    if category == 'Poster':
      title_node = xml.find('mods:title')
      authorname_node = xml.find('mods:namePart')
      modstopic_node = xml.find('mods:topic')
      title_node.string = record.Title
      authorname_node.string = record.Author
      modstopic_node.string = record.Keywords

  with open(OUTPUT_FILE.format(record.Title.replace(',','').replace(' ','').replace('/','')),'w') as f:
    f.write(str(xml))


if __name__ == '__main__':
  records, category = get_records()

  for record in records:
    output_one(record, category)
