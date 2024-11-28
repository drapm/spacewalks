from eva_data_analysis import text_to_duration

def test_text_to_duration_float1():
    input_value = "10:15"
    assert text_to_duration(input_value) == 10.25

def test_text_to_duration_float2():
    input_value = "10:20"
    assert abs(text_to_duration(input_value) - 10.333333) < 1e-5

def test_text_to_duration_integer():
    input_value = "10:00"
    assert text_to_duration(input_value) == 10

test_text_to_duration_float1()
test_text_to_duration_float2()
test_text_to_duration_integer()
