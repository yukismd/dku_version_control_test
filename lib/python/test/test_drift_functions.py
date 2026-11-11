import math
import dku_libs
import random

def test_drift_integer_working():
    # Standard cases, just controlling it does not fail
    before_value = 9
    after_value = dku_libs.drift_integer(before_value)
    
    before_value = 0
    after_value = dku_libs.drift_integer(before_value)
    
    before_value = -9
    after_value = dku_libs.drift_integer(before_value)
    
    before_value = 999999999999999
    after_value = dku_libs.drift_integer(before_value)
    print(f"Integer Drift edge cases are all OK")

def test_drift_integer_option_proba():
    dku_libs.init_drift()
    test_size = 1000
    drift_expected = 0.3
    randomlist = random.sample(range(-1000, 1000), test_size)
    has_drifted = 0
    for i in randomlist :
        new = dku_libs.drift_integer(i,drift_proba=drift_expected)
        if new != i :
            has_drifted = has_drifted + 1
        #print(f"{i} to {new}=> {has_drifted}")
    drift_actual = has_drifted / test_size
    assert abs(drift_actual - drift_expected) < 0.05, f"Probability to drift is not working: expected {drift_expected*100}% of values would drift, actually got {drift_actual*100}%"
    print(f"Probability to drift is working : expected {drift_expected*100}% of values would drift, actually got {drift_actual*100}%")

def test_drift_integer_option_percent():
    dku_libs.init_drift()
    test_size = 1000
    drift_proba = 1
    max_drift_percent_expected = 0.2
    randomlist = random.sample(range(-1000, 1000), test_size)
    total_drift = 0
    nb_drift = 0
    for i in randomlist :
        new = dku_libs.drift_integer(i, drift_proba = drift_proba , max_drift_percent = max_drift_percent_expected)
        if i == 0 or new == 0:
            continue
        drift_percent_actual = abs( (new -i) / i )
        nb_drift = nb_drift + 1
        total_drift = total_drift + drift_percent_actual
    
    avg_drift_percent = total_drift / nb_drift
    assert avg_drift_percent <=  max_drift_percent_expected , f"Drift percent is not working: expected max drift of {max_drift_percent_expected*100}% of values would drift, actually got {drift_percent_actual*100}% ( {i} => {new})"
    print(f"Drift percent is working: expected max drift of {max_drift_percent_expected*100}% of values would drift, actually got {drift_percent_actual*100}% ( {i} => {new})")
    # way
    #precision
    
def test_drift_numeric_edge_cases():
    #val is Nan : should work and interpreted as 0
    after_value = dku_libs.drift_numeric(math.nan)
    assert after_value == 0, f"Nan values should return 0 but got {after_value}"
    
    #val is non-numeric (string)

