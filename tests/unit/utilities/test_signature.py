import pytest

from kwil._utils.signature import sign


@pytest.mark.parametrize(
    "data, expected",
    [
        (
            b"12345",
            "ce4b9bbf9fbc5204d7e17818416c6497c48d7209ee0edd06e8c8ca31cc3ba55f2b51efa977df44987a8014f69137f11880e8590c0aa600e46b2f8534a2ff40dc01",
        ),
        (
            b"1234567890",
            "33120038417a9fc9c3bb9665037bcc67a58eebc1192d6f7d2502f56adeb147ef39eae64577e7e50c28e63d6a33d0d4891693e0aa071a0a565aba971eb7b08f8101",
        ),
        (
            b"xdeg",
            "12c81eb51fadbfb43eeffd6503714ba5beb890a3bed373841bc8d552985bf1847103b09703aa00ce0743b4c3977ee668198203f205628f10905ec470cebea30300",
        ),
    ],
)
def test_sign(private_key, data, expected):
    signature = sign(data, private_key)
    assert signature["signature_bytes"].hex() == expected
