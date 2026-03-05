from logic_utils import check_guess
from app import get_range_for_difficulty

def test_difficulty_ranges_min_is_1():
    # All difficulties should have a minimum of 1
    assert get_range_for_difficulty("Easy")[0] == 1
    assert get_range_for_difficulty("Normal")[0] == 1
    assert get_range_for_difficulty("Hard")[0] == 1

def test_difficulty_ranges_max():
    # Easy max=20, Normal max=50, Hard max=100
    assert get_range_for_difficulty("Easy")[1] == 20
    assert get_range_for_difficulty("Normal")[1] == 50
    assert get_range_for_difficulty("Hard")[1] == 100

def test_difficulty_ranges_increase():
    # Easy should have fewer numbers than Normal, Normal fewer than Hard
    easy_range = get_range_for_difficulty("Easy")[1] - get_range_for_difficulty("Easy")[0]
    normal_range = get_range_for_difficulty("Normal")[1] - get_range_for_difficulty("Normal")[0]
    hard_range = get_range_for_difficulty("Hard")[1] - get_range_for_difficulty("Hard")[0]
    assert easy_range < normal_range < hard_range

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result[0] == "Win"
    assert result[1] == "🎉 Correct!"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result[0] == "Too High"
    assert result[1] == "📉 Go LOWER!"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result[0] == "Too Low"
    assert result[1] == "📈 Go HIGHER!"
