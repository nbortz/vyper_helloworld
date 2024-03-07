# This is a simple Vyper contract that returns "Hello World" when the hello() function is called.

@external
@view
def hello() -> String[11]:
    return "Hello World"
