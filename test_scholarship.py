from scholarship_checker import is_eligible_for_scholarship


def test_eligible_for_scholarship():
    assert is_eligible_for_scholarship(3.50, 20000) is True
    assert is_eligible_for_scholarship(3.25, 19000) is True
    assert is_eligible_for_scholarship(3.00, 18000) is True
    assert is_eligible_for_scholarship(2.75, 17000) is True
    assert is_eligible_for_scholarship(2.50, 16000) is True
    assert is_eligible_for_scholarship(2.25, 15000) is True
    assert is_eligible_for_scholarship(2.00, 14000) is True
    assert is_eligible_for_scholarship(1.75, 13000) is True
    assert is_eligible_for_scholarship(1.50, 12000) is True
    assert is_eligible_for_scholarship(1.25, 11000) is True
    assert is_eligible_for_scholarship(1.00, 10000) is True


def test_not_eligible_due_to_GPA():
    assert is_eligible_for_scholarship(3.75, 24000) is False
    assert is_eligible_for_scholarship(4.0, 21000) is False
    assert is_eligible_for_scholarship(4.75, 22000) is False
    assert is_eligible_for_scholarship(5.0, 23000) is False
