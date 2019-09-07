from nose.tools import *
from ex48 import lexicon
#from ex48 import parser as p
from ex48.parser import ParserError, Parser

def setup():
    print("SETUP!")

def teardown():
    print("TEAR DOWN!")

def test_parser_sv():
    subj = Parser().parse_sentence([('verb', 'run'), ('direction', 'north')])
    assert_equal(subj.subject, 'player')
    assert_equal(subj.object, 'north')
    assert_equal(subj.verb, 'run')

def test_parser_svo():
    subj = Parser().parse_sentence([('noun', 'bear'), ('verb', 'eat'),
    ('stop', 'the'), ('noun', 'honey')])
    assert_equal(subj.subject, 'bear')
    assert_equal(subj.object, 'honey')
    assert_equal(subj.verb, 'eat')

def test_parser_s():
    with assert_raises(ParserError) as error:
        subj = Parser().parse_sentence([('noun', 'bear')])
    assert_equal(error.exception.message, 'Expected a verb next.')

def test_user_input():
    #data = input('Please enter a word: ')
    #result = lexicon.scan(data)
    pass
