from eva_data_analysis import text_to_duration
import pytest

def test_text_to_duration_float1():
    """
    Test that text_to_duration returns expected ground truth values for typical
    durations with a non-zero minute component but where the decimal representation
    of the minute component is rational
    """
    input_value = "10:15"
    assert text_to_duration(input_value) == pytest.approx(10.25)

def test_text_to_duration_float2():
    """
    Test that text_to_duration returns expected ground truth values for typical
    durations with a non-zero minute component
    """
    input_value = "10:20"
    assert text_to_duration(input_value) == pytest.approx(10.333333)

def test_text_to_duration_integer():
    input_value = "10:00"
    assert text_to_duration(input_value) == 10
