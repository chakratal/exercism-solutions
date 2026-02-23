"""Functions for implementing the rules of the classic arcade game Pac-Man."""

def eat_ghost(power_pellet_active, touching_ghost):
    """
    Verify Pac-Man can eat a ghost if empowered by a power pellet.
    
    :param power_pellet_active: bool - does  player have active power pellet?
    :param touching_ghost: bool - is player touching a ghost?
    :return: bool
    """

    return power_pellet_active and touching_ghost

def score(touching_power_pellet, touching_dot):
    """
    Verify Pac-Man scored when a power pellet or dot has been eaten.
    
    :param touching_power_pellet: bool - is player touching a power pellet?
    :param touching_dot: bool - is player touching a dot?
    :return: bool - has player scored?
    """

    return touching_power_pellet or touching_dot

def lose(power_pellet_active, touching_ghost):
    """
    Trigger GAME OVER when Pac-Man touches a ghost without his power pellet.
    
    :param power_pellet_active: bool - does player have active power pellet?
    :param touching_ghost: bool - is player touching a ghost?
    :return: bool - has player lost the game?
    """

    return not power_pellet_active and touching_ghost

def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    """Trigger victory when all dots have been eaten.

    :param has_eaten_all_dots: bool - has player eaten all dots?
    :param power_pellet_active: bool - does player have active power pellet?
    :param touching_ghost: bool - is player touching a ghost?
    :return: bool - has player won the game?
    """

    return has_eaten_all_dots and not (not power_pellet_active and touching_ghost)