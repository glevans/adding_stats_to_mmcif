#!/usr/bin/env python

import logging                          # Import the logging module to enable logging of messages.
import os                               # Import the os module to interact with the operating system.
import xml.etree.ElementTree as ET      # Import the ElementTree module for parsing XML data.
import argparse                         # Import parser for command-line options, arguments and subcommands

def parse_xml(xml_file):
    """
    Checks if the input file is an XML file and parses it.
    :param xml_file: Path to the XML file.
    :return: Root of the XML tree or None if an error occurs.
    """

    root = None
    try:
        if os.path.exists(xml_file):        # Check if the XML file exists.
            tree = ET.parse(xml_file)       # Parse the XML file 
            root = tree.getroot()           # Get the root element of the XML tree.
        else:
            logging.error('xml file: "{}" does not exist'.format(xml_file))                  # Log an error message if the XML file does not exist.
    
    except ET.ParseError as pe:
        logging.error('Failed to parse XML file: "{}". Error: {}'.format(xml_file, pe))      # Log a specific error message for parsing errors.
    
    except Exception as e:
        logging.error(e)                                                                     # Log any exceptions that occur during parsing -- aka file is not a properly formatted xml file.

    return root

if __name__ == '__main__':
## This block runs only if the script is executed directly.
    
    # Argument parser setup for command-line execution
    parser = argparse.ArgumentParser(description='Parse an XML file and print its root element.')
    parser.add_argument('--xml_file', help='Path to the XML file', type=str, required=True)
    parser.add_argument('-d', '--debug', help='Enable debugging', action='store_const', dest='loglevel', const=logging.DEBUG, default=logging.INFO)

    args = parser.parse_args()

    # Set the logging level based on the debug argument
    logging.basicConfig(level=args.loglevel)
    
    FILE_ROOT = os.path.dirname(os.path.realpath(__file__))                   # Get the directory of the current script file.
    package_path = os.path.dirname(os.path.join(FILE_ROOT, '..', '..', ))     # Determine the package path by going up two levels from the script directory.
    test_data = os.path.join(package_path, 'test_data')                       # Construct the path to the 'test_data' directory.
    example_file = os.path.join(test_data, "good_example.xml")                # Construct the path to the example XML file
    
    data1 = parse_xml(xml_file=args.xml_file)                             # Parse the example XML file and store the root element
    print("output from improvements")
    print(data1) # Print the root element of the parsed XML file.
    print()

    data2 =  parse_xml(xml_file=example_file)                             # Parse the example XML file and store the root element
    print("original output from improvements")
    print(data2) # Print the root element of the parsed XML file.
