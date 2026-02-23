def eat_ghost(power_pellet_active, touching_ghost):
    """
    :param power_pellet_active: bool - does  player have active power pellet?
    :param touching_ghost: bool - is player touching a ghost?
    :return: bool
    """

    return power_pellet_active and touching_ghost

def score(touching_power_pellet, touching_dot):
    """
    :param touching_power_pellet: bool - is player touching a power pellet?
    :param touching_dot: bool - is player touching a dot?
    :return: bool - has player scored?
    """

    return touching_power_pellet or touching_dot

def lose(power_pellet_active, touching_ghost):
    """
    :param power_pellet_active: bool - does player have active power pellet?
    :param touching_ghost: bool - is player touching a ghost?
    :return: bool - has player lost the game?
    """

    return not power_pellet_active and touching_ghost

def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    """Trigger the victory event when all dots have been eaten.

    :param has_eaten_all_dots: bool - has the player "eaten" all the dots?
    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool - has the player won the game?
    """

    return has_eaten_all_dots and not (not power_pellet_active and touching_ghost)