from cubert import cubert
from randomseed import getrandomseed
# import sys
def solve_god(cube):
    #
    cubes = [cube]
    solved_cube = cubert()
    movess = [""]
    moves = "wogrby"
    appendix = ["","'","2"]
    previous_cube_states = set()
    while(len(cubes)>0):
        current_cube = cubes.pop(0)
        current_moves = movess.pop(0)
        #graphical output
        if(current_cube.cube == solved_cube.cube):
            #solved
            return current_moves
        else:
            previous_cube_states.add(str(current_cube.cube))
            for m in moves:
                for app in appendix:
                    next_cube = cubert(current_cube)
                    next_cube.run_moves(m+app)
                    if str(next_cube.cube) not in previous_cube_states:
                        cubes.append(next_cube)
                        movess.append(current_moves+m+app)
                        
    


def main():
    #user input
    command = getrandomseed(4)
    print("seed: ",command)
    cube = cubert(command)
    cube.print_cube()
    print("Solving...")
    solution = solve_god(cube)
    print("solution:",solution)
            
if __name__ == "__main__":
    main()