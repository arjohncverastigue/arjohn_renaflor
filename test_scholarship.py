from scholarship_checker import is_eligible_for_scholarship


def test_eligible_senior():
    assert is_eligible_for_scholarship(3.50) is True
    assert is_eligible_for_scholarship(3.25) is True
    assert is_eligible_for_scholarship(3.00) is True
    assert is_eligible_for_scholarship(2.75) is True
    assert is_eligible_for_scholarship(2.50) is True
    assert is_eligible_for_scholarship(2.25) is True
    assert is_eligible_for_scholarship(2.00) is True
    assert is_eligible_for_scholarship(1.75) is True
    assert is_eligible_for_scholarship(1.50) is True
    assert is_eligible_for_scholarship(1.25) is True
    assert is_eligible_for_scholarship(1.00) is True


def test_not_eligible_due_to_GPA():
    assert is_eligible_for_scholarship(3.75) is False
    assert is_eligible_for_scholarship(4.0) is False
    assert is_eligible_for_scholarship(4.75) is False
    assert is_eligible_for_scholarship(5.0) is False
    