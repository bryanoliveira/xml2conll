from xml.dom import minidom
import argparse
import nltk
nltk.download('punkt')

# Parse inline arguments
parser = argparse.ArgumentParser(description='XML to Conll converter')
parser.add_argument('--input', type=str, default='datasets/harem/miniHAREM.xml',
                    help='The XML file to convert')
parser.add_argument('--output', type=str,
                    help='The output CONLL file name')
args = parser.parse_args()

# Read XML input file
xmldoc = minidom.parse(args.input)
docs = xmldoc.getElementsByTagName('DOC')
print('Converting ' + str(len(docs)) + ' documents')


# Scan all the docs searching for text and their tags
def scandown(elements, categ, output):
    global lines
    for el in elements:
        if el.nodeName == '#text':
            first = True
            for token in nltk.word_tokenize(el.nodeValue):
                output.write(token + ' ' + categ + '\n')
                lines += 1

        scandown(
            el.childNodes,
            el.attributes['CATEG'].value if el.attributes and 'CATEG' in el.attributes else 'O',
            output
        )


lines = 0
output_file_name = args.input.split(
    'xml')[0] + 'conll' if not args.output else args.output
with open(output_file_name, 'a') as output:
    last_category = False
    scandown(docs, 'O', output)

print('%d lines written' % lines)
