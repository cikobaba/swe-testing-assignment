from quick_calc.session import QuickCalcSession


def test_full_user_interaction_addition():
    s = QuickCalcSession()
    s.press_digit("5")
    s.press_operator("+")
    s.press_digit("3")
    s.press_equals()
    assert s.display == "8"


def test_clear_resets_after_calculation():
    s = QuickCalcSession()
    s.press_digit("9")
    s.press_operator("*")
    s.press_digit("9")
    s.press_equals()
    assert s.display == "81"

    s.press_clear()
    assert s.display == "0"