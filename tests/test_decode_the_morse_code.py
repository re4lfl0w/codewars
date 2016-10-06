import pytest

from kata.decode_the_morse_code import decode_morse_my1, decode_morse_best

test_data = [
    ('.... . -.--   .--- ..- -.. .', 'HEY JUDE'),
    ('... --- ...', 'SOS'),
    ('...---...', 'SOS'),
    (' . ', 'E'),
    ('   .   . ', 'E E'),
    ('      ...---... -.-.--   - .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-   .--- ..- -- .--. ...   --- ...- . .-.   - .... .   .-.. .- --.. -.--   -.. --- --. .-.-.-  ',
     'SOS! THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.'),
    ('-.-.--', '!'),
]


class TestClass(object):
    @pytest.mark.parametrize('input_, expected', test_data)
    def test_decode_morse_my1(self, input_, expected):
        assert decode_morse_my1(input_) == expected

    @pytest.mark.parametrize('input_, expected', test_data)
    def test_decode_morse_best1(self, input_, expected):
        assert decode_morse_best(input_) == expected