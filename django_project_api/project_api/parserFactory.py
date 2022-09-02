from parser import Parser
from parsers import *


class ParserFactory(object):

    def parser(self, parser_type):
        parser = self.get_parser(parser_type)
        return parser

    def get_parser(self, parser_type):
        parsers_classes = Parser.__subclasses__()
        parser_type_formatted = parser_type.lower()
        parsers_classes_formatted = []

        for parser_class in parsers_classes:
            parsers_classes_formatted.append(parser_class.__name__.lower())

        if parser_type_formatted in parsers_classes_formatted:
            parser = parsers_classes[parsers_classes_formatted.index(parser_type)]()
            return parser
        else:
            raise Exception("Value Error")
