"""This function determines how Bob will respond when people say something to him or ask him a question."""

def response(hey_bob):
    hey_bob = hey_bob.rstrip()
    if len(hey_bob) == 0 or hey_bob.isspace():
        return "Fine. Be that way!"
    elif hey_bob.isupper() and hey_bob[-1] == "?":
        return "Calm down, I know what I'm doing!"
    elif hey_bob[-1] == "?":
        return "Sure."
    elif hey_bob.isupper():
        return "Whoa, chill out!"
    else:
        return "Whatever."