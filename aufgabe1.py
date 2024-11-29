import yaml
import argparse
import numpy
import os
import argparse




#returns beginning city
def get_beginning(problem: dict) -> str:
    return problem['problem']['city_start']

#returns ending city
def get_end(problem: dict) -> str:
    return problem['problem']['city_end']

#returns all the children from
def get_children(problem: dict, city: str) -> list:
    city_with_city = get_city_with_city(problem, city)
    return problem['problem'][city_with_city]['connects_to']


def get_city_with_city(problem: dict, just_the_city: str) -> dict:

    city_with_city = "NO_CITY_FOUND"

    cities = problem['problem']

    for c in cities:
        if (just_the_city + "_city") == c:
            city_with_city = c
            break

        if ("city_" + just_the_city) == c:
            city_with_city = c
            break

    return city_with_city


    return 'NO PARENT FOUND'

def sort_1(frontier) -> list[tuple[str, int]]:
    frontier = sorted(frontier, key=lambda x: x[1])        #idk how it works, but it works. SO DONT TOUCH IT
    return frontier

def print_solution_to_file_1(problem: dict, cost: float, path, expanded_nodes_count: int):

    output_file_path = "aufgabe1-1.yaml"

    with open(output_file_path, "w") as file:
        file.write("solution: \n")
        file.write("  cost: " + str(cost) + "\n")
        file.write("  expanded_nodes: " + str(expanded_nodes_count) + "\n")
        file.write("  heuristic: \n")
        for city in problem['problem']['cities']:
            file.write("    " + get_city_with_city(problem, city) + ": 0.0" +"\n")
            #print("    " + city + "\n")

        file.write("  path: \n")

        for city in path:
            file.write("  - " + city + "\n")


    return



def get_heuristics(problem: dict, city: str):
    # print(city) #21
    line_of_sight: float = problem['additional_information'][get_city_with_city(problem, city)]['line_of_sight_distance']
    height: float = problem['additional_information'][get_city_with_city(problem, city)]['altitude_difference']

    #MAYBE 0.1*height???
    #return line_of_sight + height #WRONG
    return line_of_sight + 0.5*height
    


def print_solution_to_file_3(cost: float, path, expanded_nodes_count: int, heuristics: dict):

    output_file_path = "aufgabe1-3.yaml"

    with open(output_file_path, "w") as file:
        file.write("solution: \n")
        file.write("  cost: " + str(cost) + ".0" "\n")
        file.write("  expanded_nodes: " + str(expanded_nodes_count))
        file.write("\n  heuristic: \n" )

        for city, heuristic in heuristics.items():
            file.write("    " + get_city_with_city(problem, city) + ": " + str(heuristic) + "\n")

        file.write("  path: \n")


        for city in path:
            file.write("  - " + city + "\n")

        



    return



def solution_path_3(problem, explored_set, start_city, end_city, expanded_nodes_count: int, heuristics: dict):
    path = []
    node = end_city
    cost = 0

    #print(explored_set)

    while node != start_city:
        path.append(node)
        parent = explored_set[node]['parent']

        cost_of_child = get_children(problem, parent)[node]
        cost = cost + cost_of_child

        node = parent

    path.append(start_city)
    path.reverse()

    print_solution_to_file_3(cost, path, expanded_nodes_count, heuristics);



    return


def solution_path_1(problem, explored_set, start_city, end_city, expanded_nodes_count: int):
    path = []
    node = end_city
    cost = 0

    #print(explored_set)

    while node != start_city:
        path.append(node)
        parent = explored_set[node]['parent']

        cost_of_child = get_children(problem, parent)[node]
        cost = cost + cost_of_child

        node = parent

    path.append(start_city)
    path.reverse()

    print_solution_to_file_1(problem, cost, path, expanded_nodes_count);



    return

def check_if_node_is_end(node: str, end: str) -> bool:
    if(node == end):
        return True
    return False







def solution_path_2(problem, explored_set, start_city, end_city, expanded_nodes_count: int, heuristics: dict):
    path = []
    node = end_city
    cost = 0

    #print(explored_set)

    while node != start_city:
        path.append(node)
        parent = explored_set[node]['parent']

        cost_of_child = get_children(problem, parent)[node]
        cost = cost + cost_of_child

        node = parent

    path.append(start_city)
    path.reverse()

    print_solution_to_file_2(cost, path, expanded_nodes_count, heuristics, explored_set);



    return






def sort_2(frontier) -> list[tuple[str, int]]:
    frontier = sorted(frontier, key=lambda x: x[1] + x[2])        #idk how it works, but it works. SO DONT TOUCH IT
    return frontier

def print_solution_to_file_2(cost: float, path, expanded_nodes_count: int, heuristics: dict, explored_set):

    output_file_path = "aufgabe1-2.yaml"

    with open(output_file_path, "w") as file:
        file.write("solution: \n")
        file.write("  cost: " + str(cost) + ".0" "\n")
        file.write("  expanded_nodes: " + str(expanded_nodes_count))

        file.write("\n  heuristic: \n" )

        for city, heuristic in heuristics.items():
            file.write("    " + get_city_with_city(problem, city) + ": " + (str(heuristic)) + ".0" + "\n")
   

        file.write("  path: \n")
 
        for city in path:
            file.write("  - " + city + "\n")

    return


def get_line_of_sight(problem: dict, city: str):
    #print(city) #21
    return problem['additional_information'][get_city_with_city(problem, city)]['line_of_sight_distance']













def ucs(problem):

    start_city: str = get_beginning(problem)
    end_city: str = get_end(problem)

    frontier: list[tuple] = [(start_city, 0)]

    explored_set: dict = {start_city: {'parent': None, 'cost': 0}}
    expanded_nodes_count = 0

    while True:
        if (len(frontier) == 0):
            raise ValueError("ValueError")

        frontier = sort_1(frontier)
        #print(frontier)
        node, path_cost = frontier.pop(0)
        expanded_nodes_count = expanded_nodes_count + 1
        #idk if the lower one works



        #print(node)
        #print(end_city)

        if check_if_node_is_end(node, end_city):
            #print(expanded_nodes_count)
            #print(explored_set)
            
            return solution_path_1(problem, explored_set, start_city, end_city, expanded_nodes_count-1)

        for child, cost in get_children(problem, node).items():
            total_cost = path_cost + cost
            if child not in explored_set or total_cost < explored_set[child]['cost']:
                frontier.append((child, total_cost))
                # frontier = sort(frontier) #bad!
                explored_set[child] = {'parent': node, 'cost': total_cost}




    return




def shitty_a_star(problem):

    start_city: str = get_beginning(problem) #0
    end_city: str = get_end(problem)           #11

    heuristics = {city: get_line_of_sight(problem, city) for city in problem['problem']['cities']}

    frontier: list[tuple] = [(start_city, 0, heuristics[start_city])]
    
    explored_set: dict = {start_city: {'parent': None, 'cost': 0}}
    expanded_nodes_count = 0

    while True:
        if (len(frontier) == 0):
            raise ValueError("ValueError")

        frontier = sort_2(frontier)
        #print(frontier)
        node, path_cost, heuristic = frontier.pop(0)
        expanded_nodes_count = expanded_nodes_count + 1
        #idk if the lower one works



        #print(node)
        #print(end_city)

        if check_if_node_is_end(node, end_city):
            #print(expanded_nodes_count)
            return solution_path_2(problem, explored_set, start_city, end_city, expanded_nodes_count-1, heuristics)

        for child, cost in get_children(problem, node).items():
            total_cost = path_cost + cost
            heuristic_cost = heuristics[child]
            if child not in explored_set or total_cost < explored_set[child]['cost']:
                frontier.append((child, total_cost, heuristic_cost))
                # frontier = sort(frontier) #bad!
                explored_set[child] = {'parent': node, 'cost': total_cost}




    return


def not_so_shitty_a_star(problem):

    start_city: str = get_beginning(problem) #0
    end_city: str = get_end(problem)           #11

    heuristics = {city: get_heuristics(problem, city) for city in problem['problem']['cities']}
    frontier: list[tuple] = [(start_city, 0, heuristics[start_city])]


    explored_set: dict = {start_city: {'parent': None, 'cost': 0}}
    expanded_nodes_count = 0


    while True:
        if (len(frontier) == 0):
            raise ValueError("ValueError")

        frontier = sort_2(frontier)
        #print(frontier)
        node, path_cost, heuristic = frontier.pop(0)
        expanded_nodes_count = expanded_nodes_count + 1
        #idk if the lower one works



        #print(node)
        #print(end_city)

        if check_if_node_is_end(node, end_city):
            #print(expanded_nodes_count)
            return solution_path_3(problem, explored_set, start_city, end_city, expanded_nodes_count-1, heuristics)

        for child, cost in get_children(problem, node).items():
            total_cost = path_cost + cost
            heuristic_cost = heuristics[child]
            if child not in explored_set or total_cost < explored_set[child]['cost']:
                frontier.append((child, total_cost, heuristic_cost))
                # frontier = sort(frontier) #bad!
                explored_set[child] = {'parent': node, 'cost': total_cost}




    return

if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("filename", help="usage: python3 aufgabe1.py problem.yaml")
    args = parser.parse_args()


    # checks if the file exists
    if os.path.isfile(args.filename) == False:
        raise ValueError("ValueError")

    # stores the command line parameter (name of file) into "filename"
    filename = parser

    #print(args.filename)

    ###DELETE THIS WHEN YOU ARE FINISHED WITH TESTING
    #filename = "test_large.yaml"
    with open(args.filename, "r") as file:
        problem = yaml.safe_load(file)

    ucs(problem)
    shitty_a_star(problem)
    not_so_shitty_a_star(problem)

#explored_set = set()
#len(explored_set)