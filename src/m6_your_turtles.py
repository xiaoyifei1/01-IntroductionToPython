"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Yifei Xiao.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# TODO: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
import rosegraphics as rg


window = rg.TurtleWindow()

will = rg.SimpleTurtle('turtle')
will.pen = rg.Pen('green', 1)
will.speed = 50


size = 300
sin = rg.SimpleTurtle('turtle')
sin.pen = rg.Pen('blue', 1 )
sin.speed = 50

for k in range(9):

    size = size - 12
    will.draw_square(size)
    will.pen_up()
    will.forward(10)
    will.pen_down()
    size = size - 10

    size = size - 12
    sin.draw_square(size)
    sin.pen_up()

    sin.forward(10)
    sin.pen_down()
    size = size - 10

window.close_on_mouse_click()