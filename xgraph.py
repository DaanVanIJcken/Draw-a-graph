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
                    distance1 = abs(eval(function.format(x="({})".format(str(b))))
                                    - eval(function.format(x="({})".format(str(b+1)))))
                except ZeroDivisionError:
                    distance1 = 0
                except TypeError:
                    distance1 = 0
                try:
                    distance2 = abs(eval(function.format(x="({})".format(str(b))))
                                    - eval(function.format(x="({})".format(str(b-1)))))
                except ZeroDivisionError:
                    distance2 = 0
                except TypeError:
                    distance2 = 0
                distance = min([distance1, distance2])/5*3*ystep
                if distance < 0.5*ystep:
                    distance = 0.5*ystep

                # look if the pixel should be coloured
                try:
                    condition = near(eval(function.format(x="({})".format(str(b)))), a, distance)
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
    xmax_, xmin_, xstep_, ymax_, ymin_, ystep_, function_.replace('x','{x}')


if __name__ == '__main__':
    # take user inputs and make sure they are correct
    while True:
        try:
            xmax = int(input('xmax '))+1
            xmin = int(input('xmin '))
            if 0 >= xmax-xmin > 48:
                raise ValueError
        except ValueError:
            print('Those numbers are invalid.',
                  'Keep in mind that the difference can be no more than 58.',
                  sep='\n')
            continue
        break
    while True:
        try:
            xstep = int(input('xstep '))
            if xstep > xmax-xmin:
                raise ValueError
        except ValueError:
            print('That number is invalid',
                  'Keep in mind that the number has to be less than the difference between xmax and xmin.',
                  sep='\n')
            continue
        break
    while True:
        try:
            ymax = int(input('ymax '))
            ymin = int(input('ymin '))
            if 0 >= ymax-ymin > 110:        
                raise ValueError
        except ValueError:
            print('Those numbers are invalid.',
                  'Keep in mind that the difference can be no more 112',
                  sep='\n')
            continue
        break
    while True:
        try:
            ystep = int(input('ystep '))
            if ystep > ymax-ymin:
                raise ValueError
        except ValueError:
            print('That number is invalid',
                  'Keep in mind that the number has to be less than the difference between ymax and ymin.',
                  sep='\n')
            continue
        break

    # Main loop
    while True:
        # take a last bit of user input: the formula,
        # it is inside the main loop so that the user can change it later on
        while True:
            function = input("f(x) = ").lower()
            function = function.replace('x', '{x}')
            try:
                eval(function.format(x='1'))
            except SyntaxError:
                print('that is not a valid function')
                continue
            break
        
        # print the graph
        print(graph())
