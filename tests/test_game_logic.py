from logic_utils import check_guess


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"


# --- Bug fix #1: secret passed as a string must still compare correctly ---
# Previously check_guess compared an int guess to a str secret, producing
# wrong outcomes. Both are now coerced to int.

def test_string_secret_win():
    outcome, message = check_guess(50, "50")
    assert outcome == "Win"


def test_string_secret_too_high():
    # 60 > 50 even though secret arrives as the string "50"
    outcome, message = check_guess(60, "50")
    assert outcome == "Too High"


def test_string_secret_too_low():
    # 40 < 50 even though secret arrives as the string "50"
    outcome, message = check_guess(40, "50")
    assert outcome == "Too Low"


def test_string_guess_also_coerced():
    # Guess can also arrive as a string and must still compare numerically
    outcome, message = check_guess("9", "100")
    assert outcome == "Too Low"


# --- Bug fix #2: hint messages were reversed ---
# "Too High" must tell the player to go LOWER; "Too Low" must tell them
# to go HIGHER.

def test_too_high_message_says_go_lower():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message


def test_too_low_message_says_go_higher():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message
