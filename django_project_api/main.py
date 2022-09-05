from parserFactory import ParserFactory

if __name__ == '__main__':
    parser_factory = ParserFactory()
    parser = parser_factory.parser(parser_type="amazonparser")
    print(parser.parse())