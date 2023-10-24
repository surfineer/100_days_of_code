import stack

def backwards_letters():
    string = input("Enter the text you want reversed:\n")
    reversed_string = ""
    s = stack.Stack()           # stack.Stack = name of the module . class within that module
    for char in string:
        s.push(char)
    while not s.is_empty():
        reversed_string += "{}".format(s.pop())
    print(reversed_string)


string = """They have no need of our help
So do not tell me
These haggard faces could belong to you or me
Should life have dealt a different hand
We need to see them for who they really are
Chancers and scroungers
Layabouts and loungers
With bombs up their sleeves
Cut-throats and thieves
They are not
Welcome here
We should make them
Go back to where they came from
They cannot
Share our food
Share our homes
Share our countries
Instead let us
Build a wall to keep them out
It is not okay to say
These are people just like us
A place should only belong to those who are born there
Do not be so stupid to think that
The world can be looked at another way"""
print("\n".join(string.split("\n")[::-1]))