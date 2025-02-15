import pytest

from ean_tools.barcode_info import get_barcode_info, BarcodeInfo, BarcodeType


class TestBarcodeInfo:
    @pytest.mark.parametrize('ean8', ['01234567'])
    def test_get_barcode_info__ean8_restricted(self, ean8):
        assert get_barcode_info(ean8) == BarcodeInfo(
            BarcodeType.RESTRICTED_CIRCULATION, 'Used to issue Restricted Circulation Numbers within a company', None
        )

    @pytest.mark.parametrize('ean8', ['12345678'])
    def test_get_barcode_info__ean8_regular(self, ean8):
        assert get_barcode_info(ean8) == BarcodeInfo(
            BarcodeType.REGULAR, 'Used to issue GTIN-8s', None
        )

    @pytest.mark.parametrize('ean8', ['97712345'])
    def test_get_barcode_info__ean8_reserved(self, ean8):
        assert get_barcode_info(ean8) == BarcodeInfo(
            BarcodeType.RESERVED_FOR_FUTURE, 'Reserved for future use', None
        )

    @pytest.mark.parametrize('ean13', ['0000000123456'])
    def test_get_barcode_info__ean13_restricted_circulation(self, ean13):
        assert get_barcode_info(ean13) == BarcodeInfo(
            BarcodeType.RESTRICTED_CIRCULATION, 'Used to issue Restricted Ciruculation Numbers within a company', None
        )

    @pytest.mark.parametrize('ean13', ['0000001234567'])
    def test_get_barcode_info__ean13_unused(self, ean13):
        assert get_barcode_info(ean13) == BarcodeInfo(
            BarcodeType.UNUSED, 'Unused to avoid collision with GTIN-8', None
        )

    @pytest.mark.parametrize('ean13', ['0000123456789'])
    def test_get_barcode_info__ean13_regular(self, ean13):
        assert get_barcode_info(ean13) == BarcodeInfo(
            BarcodeType.REGULAR, 'GS1 US', 'us'
        )

    @pytest.mark.parametrize('ean13', ['9511234567890'])
    def test_get_barcode_info__ean13_general_manager_number(self, ean13):
        assert get_barcode_info(ean13) == BarcodeInfo(
            BarcodeType.GENERAL_MANAGER_NUMBER,
            'GS1 Global Office - General Manager Numbers for the EPC General Identifier (GID) scheme as defined by '
            'the EPC Tag Data Standard',
            None
        )

    @pytest.mark.parametrize('ean13', ['9521234567890'])
    def test_get_barcode_info__ean13_demo(self, ean13):
        assert get_barcode_info(ean13) == BarcodeInfo(
            BarcodeType.DEMO, 'GS1 Used for demonstrations and examples of the GS1 system', None
        )

    @pytest.mark.parametrize('ean13', ['9801234567890'])
    def test_get_barcode_info__ean13_refund_receipt(self, ean13):
        assert get_barcode_info(ean13) == BarcodeInfo(
            BarcodeType.REFUND_RECEIPT, 'Refund receipts', None
        )

    @pytest.mark.parametrize('ean13', ['9811234567890'])
    def test_get_barcode_info__ean13_coupon_id(self, ean13):
        assert get_barcode_info(ean13) == BarcodeInfo(
            BarcodeType.COUPON_ID, 'Used to issue GS1 coupon identification for common currency areas', None
        )

    @pytest.mark.parametrize('isbn', ['9789990700000'])
    def test_get_barcode_info__isbn_unknown(self, isbn):
        assert get_barcode_info(isbn) == BarcodeInfo(
            BarcodeType.REGULAR, 'ISBN', None
        )

    @pytest.mark.parametrize('isbn', ['9789980000000'])
    def test_get_barcode_info__isbn_known(self, isbn):
        assert get_barcode_info(isbn) == BarcodeInfo(
            BarcodeType.REGULAR, 'ISBN, Papua New Guinea', 'pg'
        )

    @pytest.mark.parametrize('ean14', ['14001234567890'])
    def test_get_barcode_info__ean14(self, ean14):
        assert get_barcode_info(ean14) == BarcodeInfo(
            BarcodeType.REGULAR, 'GS1 Germany', 'de'
        )
