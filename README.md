# xml2conll

A simple script to convert XML Named Entity Recognition annotations to the CONLL format.
This script was made to convert XMLs from the project [HAREM](https://www.linguateca.pt/HAREM/), a famous Portuguese NER dataset.
An example of input file can be found in `example.xml` or [here](https://www.linguateca.pt/aval_conjunta/HAREM/CDPrimeiroHAREMMiniHAREM.xml).

## Install

### Dependencies

You will need the following dependencies:

- Python 3

### Requirements

The following requirements will be needed. They can be installed mannually using the following list:

- nltk

Or, just by running the following command:

`pip3 install -r requirements.txt`

## Usage

Run `python3 xml2conll.py --input [XML FILE PATH]` to convert the XML file to CONLL format.
If needed, you can specify the output file name with `--output [CONLL FILE PATH]`.
