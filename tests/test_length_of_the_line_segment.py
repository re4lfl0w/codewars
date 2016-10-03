import pytest

from kata.length_of_the_line_segment import (length_of_line_my1, length_of_line_my2,
                                             length_of_line_my3, length_of_line_best)


test_data = [
        ([[0, 0], [1, 1]], "1.41"),
        ([[0, 0], [-5, -6]], "7.81"),
        ([[0, 0], [10, 15]], "18.03"),
        ([[0, 0], [5, 1]], "5.10"),
        ([[0, 0], [5, 4]], "6.40"),
        ([[0, 0], [-7, 4]], "8.06"),
        ([[0, 0], [0, 0]], "0.00"),
        ([[-3, 4], [10, 5]], "13.04"),
    ]


class TestClass(object):
    @pytest.mark.parametrize('input_, expected', test_data)
    def test_length_of_the_line_segment_my1(self, input_, expected):
        assert length_of_line_my1(input_) == expected

    @pytest.mark.parametrize('input_, expected', test_data)
    def test_length_of_the_line_segment_my2(self, input_, expected):
        assert length_of_line_my2(input_) == expected

    @pytest.mark.parametrize('input_, expected', test_data)
    def test_length_of_the_line_segment_my3(self, input_, expected):
        assert length_of_line_my3(input_) == expected

    @pytest.mark.parametrize('input_, expected', test_data)
    def test_length_of_the_line_segment_best(self, input_, expected):
        assert length_of_line_best(input_) == expected
