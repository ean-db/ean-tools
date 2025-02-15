import pytest

from ean_tools.check_digits import isbn10_has_correct_check_digit, has_correct_check_digit, get_correct_check_digit


class TestCheckDigits:
    @pytest.mark.parametrize('isbn10', ['0340013818', '9992158107', '9971502100', '0851310419'])
    def test_validate_isbn10__valid_isbns(self, isbn10):
        assert isbn10_has_correct_check_digit(isbn10)

    @pytest.mark.parametrize('isbn10', ['0684843286', '8090273415'])
    def test_validate_isbn10__invalid_isbns(self, isbn10):
        assert not isbn10_has_correct_check_digit(isbn10)

    @pytest.mark.parametrize('ean8', ['46015433', '42139362'])
    def test_validate_ean__valid_ean8(self, ean8):
        assert has_correct_check_digit(ean8)

    @pytest.mark.parametrize('upc', ['888066010726', '733739033383'])
    def test_validate_ean__valid_upc(self, upc):
        assert has_correct_check_digit(upc)

    @pytest.mark.parametrize('ean13', ['4600000001418', '8510000076278', '9788486546083'])
    def test_validate_ean__valid_ean13(self, ean13):
        assert has_correct_check_digit(ean13)

    @pytest.mark.parametrize('ean13', ['8510000076279', '9788486546080'])
    def test_validate_ean__invalid_ean13(self, ean13):
        assert not has_correct_check_digit(ean13)

    @pytest.mark.parametrize('ean,expected_check_digit', [('8510000076279', '8'), ('9788486546080', '3')])
    def test_get_correct_check_digit(self, ean, expected_check_digit):
        assert get_correct_check_digit(ean) == expected_check_digit

    @pytest.mark.parametrize('ean14', ['14260107494529', '14680211051973'])
    def test_validate_ean__valid_ean14(self, ean14):
        assert has_correct_check_digit(ean14)
