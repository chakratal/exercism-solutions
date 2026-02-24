"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
    """Verify criticality is balanced.

    :param temperature: int or float - temperature in kelvin.
    :param neutrons_emitted: int or float - number of neutrons emitted per second.
    :return: bool - is criticality balanced?

    A reactor is said to be balanced in criticality if:
    - Temperature < 800 K;
    - Neutrons_emitted > 500; and
    - Temperature * neutrons_emitted < 500000.
    """

    return temperature < 800 and neutrons_emitted > 500 and temperature * neutrons_emitted < 500000


def reactor_efficiency(voltage, current, theoretical_max_power):
    """Assess reactor efficiency zone.

    :param voltage: int or float - voltage value.
    :param current: int or float - current value.
    :param theoretical_max_power: int or float - power corresponding to 100% efficiency.
    :return: str - one of ('green', 'orange', 'red', or 'black').

    Efficiency can be grouped into 4 bands:

    1. green -> efficiency >= 80%
    2. orange -> 60% <= efficiency < 80%
    3. red -> 30% <= efficiency < 60%
    4. black ->  efficiency < 30%

    The percentage value is calculated as
    (generated_power/ theoretical_max_power)*100
    where generated_power = voltage * current
    """

    generated_power = voltage * current
    efficiency = (generated_power/ theoretical_max_power)*100

    if efficiency >= 80:
        return 'green'
    elif efficiency >= 60:
        return 'orange'
    elif efficiency >= 30:
        return 'red'
    return 'black'
    
def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Assess and return status code for the reactor.

    :param temperature: int or float - temperature in kelvin.
    :param neutrons_produced_per_second: int or float - neutron flux.
    :param threshold: int or float - threshold for category.
    :return: str - one of ('LOW', 'NORMAL', 'DANGER').

    1. 'LOW' -> `temperature * neutrons per second` < 90% of `threshold`
    2. 'NORMAL' -> `temperature * neutrons per second` +/- 10% of `threshold`
    3. 'DANGER' -> `temperature * neutrons per second` outside above-stated ranges
    """

    criticality = temperature * neutrons_produced_per_second
    if criticality < (threshold * .9):
        return 'LOW'
    elif criticality <= (threshold * .1) or criticality <= (threshold * 1.1):
        return 'NORMAL'
    return 'DANGER'
