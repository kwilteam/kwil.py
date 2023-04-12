from kwil._utils.dataset import generate_dbi


def test_generate_dbi():
    dbi = generate_dbi("0xc89D42189f0450C2b2c3c61f58Ec5d628176A1E7", "demo")
    assert dbi == "x30c25f4af8d4ca7f0fc30d4d9d1e2822cb0feca22260a2d2fcf7b011"
