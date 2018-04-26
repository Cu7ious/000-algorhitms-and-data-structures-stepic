#! /usr/bin/env python3
pp = __import__('000-parentheses').parenth_parser

try:
    string = "([](){([])})"
    result = pp(string)
    exp = "Success"
    assert result is exp

    string = "()[]}"
    result = pp(string)
    exp = 5
    assert result is exp

    string = "{{[()]]"
    result = pp(string)
    exp = 7
    assert result is exp

    string = "{{{[][][]"
    result = pp(string)
    exp = 3
    assert result is exp

    string = "{*{{}"
    result = pp(string)
    exp = 3
    assert result is exp

    string = "[[*"
    result = pp(string)
    exp = 2
    assert result is exp

    string = "{*}"
    result = pp(string)
    exp = "Success"
    assert result is exp

    string = "{{"
    result = pp(string)
    exp = 2
    assert result is exp

    string = "{}"
    result = pp(string)
    exp = "Success"
    assert result is exp

    string = ""
    result = pp(string)
    exp = "Success"
    assert result is exp

    string = "}"
    result = pp(string)
    exp = 1
    assert result is exp

    string = "*{}"
    result = pp(string)
    exp = "Success"
    assert result is exp

    string = "{{{**[][][]"
    result = pp(string)
    exp = 3
    assert result is exp

    string = "{"
    result = pp(string)
    exp = 1
    assert result is exp

    string = "{[}"
    result = pp(string)
    exp = 3
    assert result is exp

except AssertionError:
    print("{} -> Expected: {}, Got: {}".format(string, exp, result))
    raise
