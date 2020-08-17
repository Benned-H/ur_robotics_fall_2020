# Author: Samuel Triest and Benned Hedegaard
# Last revised 7/7/2020

from time import sleep
from math import pi, radians

from stepper_motors.virtual_stepper import VirtualStepper
from stepper_motors.stepper_array import StepperArray

def main():
    """Part 1: Working with one stepper motor"""
    print("\nHello! This entire file will guide you through some stepper motor examples.")
    input("When a code example is printed, press enter to run that code. (press enter to advance)")
    print("\n\n\nPart 1: Working with one stepper motor")
    
    input("s1 = VirtualStepper(n_steps = 100, delay = 1e-4) # Creates an Stepper object named s1. This will open in a new tab.") # Waits for the user to input something.
    s1 = VirtualStepper(n_steps = 100, delay = 1e-4) # Creates an Stepper object named s1. CHECK THE ACTUAL PINS (the lights on the motor driver should flash in sequence).
    input("print(type(s1)) # What should this print?")
    print(type(s1)) # What should this print?
    input("print(s1.angle) # Based on where the stepper is facing, what should this print?")
    print(s1.angle) # Read the docs. What should this print?
    

    """Part 2: Controlling the stepper"""
    print("\n\n\nPart 2: Controlling one stepper")
    input("s1.rotate_to(pi/2)")
    s1.rotate_to(pi/2)

    print("# Now flip back and forth once a second a few times.")
    input("s1.rotate_to(-pi/2)\nsleep(1)\ns1.rotate_to(pi/2)\nsleep(1)\ns1.rotate_to(-pi/2)\nsleep(1)\ns1.rotate_to(pi/2)")
    
    s1.rotate_to(-pi/2)
    sleep(1)
    s1.rotate_to(pi/2)
    sleep(1)
    s1.rotate_to(-pi/2)
    sleep(1)
    s1.rotate_to(pi/2)

    input("print(s1.angle) # What will this print now?")
    print(s1.angle) # What will this print now?
    
    
    """Part 3: More steppers"""
    print("\n\n\nPart 3: More steppers")
    
    # Just like before, we can create more Stepper objects connected to other pins.
    input("Just like before, we can create more Stepper objects connected to other pins.\ns2 = VirtualStepper(n_steps = 100, delay = 1e-4)\ns3 = VirtualStepper(n_steps = 100, delay = 1e-4)")
    s2 = VirtualStepper(n_steps = 100, delay = 1e-4)
    s3 = VirtualStepper(n_steps = 100, delay = 1e-4)
    
    text = input("Please input an integer angle (in degrees) to set all three steppers to:")
    angle = int(text)
    
    input("s1.rotate_to(radians(angle))\ns2.rotate_to(radians(angle))\ns3.rotate_to(radians(angle))")
    s1.rotate_to(radians(angle))
    s2.rotate_to(radians(angle))
    s3.rotate_to(radians(angle))
    
    
    """Part 4: Make them dance"""
    print("\n\n\nPart 4: Make them dance")

    print("For the next part of this program, you'll need to edit the code! Open three_steppers_virtual.py and go to Part 4.")
    
    # Let's say I want all three stepper motors to swap from -90 degrees to 
    # 90 degrees, every 2 seconds, three times.
    # Using the above examples, can you construct this behavior?
    
    ### YOUR CODE HERE ###
    
    return # Once you've implemented your version, REMOVE THIS LINE to allow the code to move forward.
    

    """Part 5: Renaming variables"""
    print("\n\n\nPart 5: Renaming variables")
    
    # We'll reassign the stepper motors to different variables. Try to
    # track which of the steppers will be the odd one out.
    
    # Q1: Direct assignment
    print("\nQ1: Direct assignment")
    input("s1.rotate_to(-pi/2)\ns2.rotate_to(-pi/2)\ns3.rotate_to(pi/2)")
    s1.rotate_to(-pi/2)
    s2.rotate_to(-pi/2)
    s3.rotate_to(pi/2)
    
    # Q2: Variable renaming
    print("\nQ2: Variable renaming")
    input("a = s1\nb = s2\nc = s3\na.rotate_to(pi/2)\nb.rotate_to(-pi/2)\nc.rotate_to(pi/2)")
    a = s1
    b = s2
    c = s3
    
    a.rotate_to(pi/2)
    b.rotate_to(-pi/2)
    c.rotate_to(pi/2)
    
    # Q3: More variable renaming
    print("\nQ3: More variable renaming")
    input("a = b\nb = c\nc = s1\n\na.rotate_to(pi/2)\nb.rotate_to(-pi/2)\nc.rotate_to(pi/2)")
    a = b
    b = c
    c = s1
    
    a.rotate_to(pi/2)
    b.rotate_to(-pi/2)
    c.rotate_to(pi/2)
    
    # Q4: Variables upon variables
    print("\nQ4: Variables upon variables")
    input("i = b\nj = i\nk = a\ni = k\nk = c\n\ni.rotate_to(-pi/2)\nj.rotate_to(pi/2)\nk.rotate_to(pi/2)")
    i = b
    j = i
    k = a
    i = k
    k = c
    
    i.rotate_to(-pi/2)
    j.rotate_to(pi/2)
    k.rotate_to(pi/2)
    
    
    """Part 6: Working with lists"""
    print("\n\n\nPart 6: Working with lists")
    
    input("stepper_list = [s1, s2, s3] # Create a list with the three stepper motors.")
    stepper_list = [s1, s2, s3] # Create a list with the three stepper motors.
    
    input("stepper_list[0].rotate_to(pi/2)\nstepper_list[1].rotate_to(pi/2)\nstepper_list[2].rotate_to(pi/2)")
    stepper_list[0].rotate_to(pi/2)
    stepper_list[1].rotate_to(pi/2)
    stepper_list[2].rotate_to(pi/2)

    input("We have some more code for you to write. \nLook for Part 6 and fill in the function.")

    # Can you fill in the following function? It would make our lives much easier to set all three stepper motor angles at once.
    
    def set_steppers(steppers, angles):
        """Set the angles of multiple steppers at once.

        Note: The list could have zero, or more steppers in it, not just three. How can we handle this? (recall for loops)
        
        Args:
            steppers (stepper_motors.Stepper): Steppers whose angles will be set.
            angles (list of integers): Angles to set the steppers to.
        """

        ### YOUR CODE HERE ###
        pass # Remove this once you've implemented your code.

    return # Also remove this line once you've implemented your code.
    
    input("set_steppers([s1, s2, s3], [-pi/2, -pi/2, -pi/2])")
    set_steppers([s1, s2, s3], [-pi/2, -pi/2, -pi/2])

    input("set_steppers([s1, s3], [pi/2, -pi/4])")
    set_steppers([s1, s3], [pi/2, -pi/4])

    """Part 7: Using your function"""
    print("\n\n\nPart 7: Using your function")
    input("One last coding exercise. Using your new function, can you recreate the dancing behavior from Part 4?\nNotice how much easier the job becomes.")
    
    ### YOUR CODE HERE ###

    print("And that's it. Congrats, we hope you learned something from these exercises.\nWe'll use this stepper motor interface during the next workshop to control our arm.")
    
if __name__ == "__main__":
    main()
