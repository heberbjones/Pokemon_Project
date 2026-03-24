Here's a reasonable way to split it up:

#  Tyler — Move Class
Write the Move class (constructor, get_info, and generate_attack_value methods)

# Heber — Pokemon Class
Write the Pokemon class (constructor, get_info, and heal methods)

# Carl — Main Logic
Write the main program flow: creating the 9 Move objects and 3 Pokemon objects, the random move loop, the Charmander heal demo, and the Pokemon list loop
This works well because the two classes are independent of each other, so Members 1 and 2 can work simultaneously without conflicts. Member 3 can start setting up the object creation and list logic while the other two finish their classes, then plug everything together at the end.

One tip — have all three agree on naming conventions (snake_case)