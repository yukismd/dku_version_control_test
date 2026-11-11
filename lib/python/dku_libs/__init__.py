import random
import math


def fake():
    return True


def init_drift():
    random.seed()


def drift_numeric(val, drift_proba=0.5, max_drift_percent=0.3, way=""):
    if math.isnan(val):
        val = 0

    # Randomly adjust the values by max +/- percent
    is_drift = random.random()
    if is_drift > drift_proba:
        return val

    if way == "up":
        drift = random.random() * max_drift_percent
    elif way == "down":
        drift = - random.random() * max_drift_percent
    else:
        drift = random.uniform(-1, 1) * max_drift_percent

    return val * (1 + drift)


def drift_integer(val, drift_proba=0.5, max_drift_percent=0.3, way=""):
    if math.isnan(val):
        val = 0
    return int(drift_numeric(val, drift_proba = drift_proba, max_drift_percent = max_drift_percent, way = way))


def drift_categorical(val, categories, drift_proba=0.9, ):
    print(f"Drift proba = {drift_proba}")
    is_drift = random.random()
    if is_drift < drift_proba:
        return val
    return random.choice(categories)
