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
        print(dir(metadata.exportPlaintext))
        # print(metadata.extract)
        # print(dir((metadata._Metadata__data['aspect_ratio']).description))
        for line in metadata.exportPlaintext():
            print(line)



filename = argv[1]

get_metadata(filename)

"""
metadata object attributes
['_Metadata__data', '_Metadata__header', '__bool__', '__class__', '__delattr__', 
'__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', 
'__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', 
'__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', 
'__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_logger', 'error', 'exportDictionary', 
'exportPlaintext', 'extract', 'get', 'getItem', 'getItems', 'getText', 'getValues', 'has', 'header', 
'info', 'processMovie', 'processMovieHeader', 'processTrack', 'processTrackHeader', 'quality', 
'register', 'setHeader', 'warning']
"""



