from xml.dom import minidom
import argparse
import nltk

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

# Update nltk
nltk.download('punkt')


# Map categories to BIO format
def cat2bio(category):
    global last_category
    if category == 'O':
        last_category = False
        return 'O'
    elif last_category == category:
        return 'I-' + category
    else:
        last_category = category
        return 'B-' + category

# Scan all the docs searching for text and their tags
def scandown(elements, categ, output, depth=0):
    global lines
    for el in elements:
        if el.nodeName == '#text':
            first = True
            for token in nltk.word_tokenize(el.nodeValue):
                output.write(token + ' ' + cat2bio(categ) + '\n')
                lines += 1

        scandown(
            el.childNodes,
            el.attributes['CATEG'].value if el.attributes and 'CATEG' in el.attributes else 'O',
            output,
            depth + 1
        )

    if depth == 1:
        output.write('\n')


lines = 0
output_file_name = args.input.split(
    'xml')[0] + 'conll' if not args.output else args.output
with open(output_file_name, 'a') as output:
    last_category = False
    scandown(docs, 'O', output)

print('%d lines written' % lines)
