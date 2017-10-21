from math import *
import itertools



# function that generates the graph
def graph() -> str:
    global printable
    printable = []
    for a in range(ymax, ymin, -ystep):
        for b in range(xmin, xmax, xstep):
            try:
                # to define the smallest distance between this value of x
                # and the values of x next to it,
                # and if it is smaller than 0.5 take 0,5
                # using this method graphs like x**2 will have longer lines connecting each pixel up
                try:
                    distance1 = abs(eval(function.format(x="({})".format(str(a))))
                                    - eval(function.format(x="({})".format(str(a+1)))))
                except ZeroDivisionError:
                    distance1 = 0
                except TypeError:
                    distance1 = 0
                try:
                    distance2 = abs(eval(function.format(x="({})".format(str(a))))
                                    - eval(function.format(x="({})".format(str(a-1)))))
                except ZeroDivisionError:
                    distance2 = 0
                except TypeError:
                    distance2 = 0
                distance = min([distance1, distance2])/5*3*ystep
                if distance < 0.5*ystep:
                    distance = 0.5*ystep

                # look if the pixel should be coloured
                try:
                    condition = near(eval(function.format(x="({})".format(str(a)))), b, distance)
                except ZeroDivisionError:
                    condition = False
                except TypeError:
                    condition = False            

                # look what has to be printed
                printable.append(' x' if condition else
                             (' 0' if near(b, 0, xstep/3) and near(a, 0, ystep/3) else
                              (' ═' if near(a, 0, ystep/3) else
                               ' ║' if near(b, 0, xstep/3) else '  ')))
                # look if this is the last line and if a \n is necessary
                printable.append('' if b != xmax-1 else "\n")
            except ZeroDivisionError:
                # do the same as when the error hadn't occured
                printable.append(' 0' if near(b, 0, xstep/3) and near(a, 0, ystep/3) else
                              (' ═' if near(a, 0, ystep/3) else
                               ' ║' if near(b, 0, xstep/3) else '  '))
                printable.append('' if a != xmax-1 else "\n")
            except ValueError:
                # do the same as when the error hadn't occured
                printable.append(' 0' if near(b, 0, xstep/3) and near(a, 0, ystep/3) else
                              (' ═' if near(a, 0, ystep/3) else
                               ' ║' if near(b, 0, xstep/3) else '  '))
                printable.append('' if b != xmax-1 else "\n")
    return "".join(printable)
                


# function to check whether one number is near another number
# and thus if a number is near the value of the graph at that point it should be coloured
def near(number: float, original: float, distance: float=1) -> bool:
    if number >= original-distance and number <= original+distance:
        return True
    return False

def define_variables(xmax_: int, xmin_: int, xstep_: int, ymax_: int, ymin_: int, ystep_: int, function_: str):
    global xmax, xmin, xstep, ymax, ymin, ystep, function
    xmax, xmin, xstep, ymax, ymin, ystep, function = \
    xmax_, xmin_, xstep_, ymax_, ymin_, ystep_, function_.replace('y','{x}')
