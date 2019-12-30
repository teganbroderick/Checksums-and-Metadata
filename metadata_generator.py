#metadata generator for video files

from hachoir.parser import createParser
from hachoir.metadata import extractMetadata
from sys import argv, stderr, exit


def get_metadata(filename):
    """extract and print metadata info for file"""
    
    parser = createParser(filename)

    if parser == None:
        print("Unable to parse file")
        return

    metadata = extractMetadata(parser)

    if metadata == None:
        print("Unable to extract metadata")
        return
    else:
        # print(dir(metadata))
        for line in metadata.exportPlaintext():
            print(line)


filename = argv[1]

get_metadata(filename)



