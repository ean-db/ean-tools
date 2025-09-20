import pytest

from ean_tools.normalization import convert_isbn10_to_isbn13, normalize_barcode


class TestNormalizeBarcode:
    @pytest.mark.parametrize('barcode', ['test', '', '   ', '123456789X', '00000000', '0₇4509947290₀'])
    def test_normalize_barcode__invalid_barcodes(self, barcode):
        with pytest.raises(ValueError, match="Doesn't look like a barcode"):
            normalize_barcode(barcode)

    @pytest.mark.parametrize('barcode,expected_normalized_barcode', [
        (' 4\t6 0000000 1418 ', '4600000001418'), ('978-84865-4608-3', '9788486546083')
    ])
    def test_normalize_barcode__cleans_barcode(self, barcode, expected_normalized_barcode):
        assert normalize_barcode(barcode) == expected_normalized_barcode

    def test_normalize_barcode__too_short(self):
        with pytest.raises(ValueError, match='Too short for a barcode'):
            normalize_barcode('1234567')

    def test_normalize_barcode__too_long(self):
        with pytest.raises(ValueError, match='Too long for a barcode'):
            normalize_barcode('124600000001418')

    @pytest.mark.parametrize('barcode,expected_normalized_barcode', [
        ('0004600000001418', '4600000001418'), ('04600000001418', '4600000001418'), ('000001234567890', '0001234567890'),
        ('00012345678', '12345678')
    ])
    def test_normalize_barcode__strips_extra_zeros(self, barcode, expected_normalized_barcode):
        assert normalize_barcode(barcode) == expected_normalized_barcode

    @pytest.mark.parametrize('barcode', ['12345678'])
    def test_normalize_barcode__normalizes_ean8(self, barcode):
        assert normalize_barcode(barcode) == barcode

    @pytest.mark.parametrize('barcode', ['0030343420', '0060087706'])
    def test_normalize_barcode__ambiguous_isbn10_ean(self, barcode):
        with pytest.raises(ValueError, match='Ambiguous ISBN-10 / EAN'):
            normalize_barcode(barcode)

    @pytest.mark.parametrize('barcode,expected_normalized_barcode', [
        ('1402894627', '9781402894626'), ('0060087706', '9780060087708')
    ])
    def test_normalize_barcode__normalizes_valid_isbn10(self, barcode, expected_normalized_barcode):
        assert normalize_barcode(barcode, is_isbn=True) == expected_normalized_barcode

    @pytest.mark.parametrize('barcode,expected_normalized_barcode', [
        ('1402894627', '9781402894626')
    ])
    def test_normalize_barcode__normalizes_guessed_isbn10(self, barcode, expected_normalized_barcode):
        assert normalize_barcode(barcode) == expected_normalized_barcode

    @pytest.mark.parametrize('barcode', ['4600000001418', '0030343420'])
    def test_normalize_barcode__invalid_isbn(self, barcode):
        with pytest.raises(ValueError, match='Invalid ISBN'):
            normalize_barcode(barcode, is_isbn=True)

    @pytest.mark.parametrize('barcode', [
        '9781408300008', '0602445046027', '0028941961426', '0004408039426', '0000768425527'
    ])
    def test_normalize_barcode__preserves_valid_barcodes(self, barcode):
        assert normalize_barcode(barcode) == barcode

    @pytest.mark.parametrize('isbn10,isbn13', [
        ('1402894627', '9781402894626'), ('0198526636', '9780198526636')
    ])
    def test_convert_isbn10_to_isbn13(self, isbn10, isbn13):
        assert isbn13 == convert_isbn10_to_isbn13(isbn10)
