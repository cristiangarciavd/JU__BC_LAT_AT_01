import unittest
from parserFactory import ParserFactory
from custom_exceptions import InvalidParserFactoryOption, MultipleValuesParserFactoryClass


class TestParserFactory(unittest.TestCase):

    def test_return_amazonparser_object(self):
        parser_factory = ParserFactory()
        parser = parser_factory.parser('amazonparser')
        self.assertEqual(type(parser).__name__, 'AmazonParser')

    def test_return_aliexpressparser_object(self):
        parser_factory = ParserFactory()
        parser = parser_factory.parser('aliexpressparser')
        self.assertEqual(type(parser).__name__, 'AliexpressParser')

    def test_return_ebayparser_object(self):
        parser_factory = ParserFactory()
        parser = parser_factory.parser('ebayparser')
        self.assertEqual(type(parser).__name__, 'EbayParser')

    def test_ebayparser_uppercase_object(self):
        parser_factory = ParserFactory()
        parser = parser_factory.parser('EbayParser')
        self.assertEqual(type(parser).__name__, 'EbayParser')

    def test_pass_invalid_value_to_parser_method(self):
        parser_factory = ParserFactory()
        with self.assertRaises(InvalidParserFactoryOption) as context:
            parser_factory.parser('')
        self.assertIn("Value is not a valid parse option", str(context.exception))

    def test_pass_no_args_in_parser_method(self):
        parser_factory = ParserFactory()
        with self.assertRaises(InvalidParserFactoryOption) as context:
            parser_factory.parser()
        self.assertIn("Value is not a valid parse option", str(context.exception))

    def test_more_than_one_arg_in_parser_method(self):
        parser_factory = ParserFactory()
        with self.assertRaises(MultipleValuesParserFactoryClass) as context:
            parser_factory.parser('one', 'two', 'three')
        self.assertIn("Multiple values are not valid", str(context.exception))
