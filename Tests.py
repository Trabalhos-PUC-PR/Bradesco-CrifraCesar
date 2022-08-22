import Cypher as cph

def test_cycle_caracter_a_to_b():
    assert cph.cycle('a') == 'b'

def test_cycle_caracter_z_to_a():
    assert cph.cycle('z') == 'a'

def test_cycle_caracter_two_times_z_to_b():
    assert cph.cycle(cph.cycle('z')) == 'b'

def test_cycle_integers():
    assert cph.cycle('1') == '2'

def test_cycle_integers_9_to_0():
    assert cph.cycle('9') == '0'

def test_cycle_integers_two_times():
    assert cph.cycle(cph.cycle('9')) == '1'

def test_cycle_upper_case_char_A_to_B():
    assert cph.cycle('A') == 'B'

def test_cycle_upper_case_char_Z_to_A():
    assert cph.cycle('Z') == 'A'

def test_cycle_upper_case_char_two_times():
    assert cph.cycle(cph.cycle('Z')) == 'B'

def test_cycle_symbols_space_to_exclamation():
    assert cph.cycle(' ') == '!'

def test_cycle_symbols_slash_to_space():
    assert cph.cycle('/') == ' '

def test_cycle_symbols_two_times():
    assert cph.cycle(cph.cycle('.')) == ' '
