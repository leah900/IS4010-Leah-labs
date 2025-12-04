from is4010_final_password_manager import store


def test_generate_default_length():
    pwd = store.generate_password()
    assert isinstance(pwd, str)
    assert len(pwd) == 16


def test_generate_custom_length_no_symbols():
    pwd = store.generate_password(length=24, use_symbols=False)
    assert len(pwd) == 24
    # Ensure no punctuation present
    import string
    assert not any(c in string.punctuation for c in pwd)
