def is_subset(a, b): # return if a is subset of b
    return set(a).issubset(set(b))

def is_proper_subset(a, b): # return if a is subset of b and they are not same
    return set(a).issubset(set(b)) and set(a) != set(b)

def find_edges(sets): # read data from input.txt
    # print("in find_edges")
    edges = []
    for i in range(len(sets)): # iter through sets
        for j in range(len(sets)):
            if i != j and is_proper_subset(sets[i], sets[j]):
                if any(is_subset(sets[i], sets[k]) and is_subset(sets[k], sets[j]) for k in range(len(sets))): # subset found: i isSub k && k isSub j: catch all cases
                    edges.append((sets[i], sets[j])) # a --(subset of)--> b
                    continue
                # edges.append((sets[i], sets[j]))
    return edges

def write_edges_to_file(edges, output_file): # write matched edges to out file
    with open(output_file, 'w') as file:
        # print("edge size = " + len(edges)
        for edge in edges:
            print(','.join(edge[0]) + '->' + ','.join(edge[1]) + '\n')
            file.write(','.join(edge[0]) + '->' + ','.join(edge[1]) + '\n')

def create_graph(input_file, output_file): # open input file, strip line by comma (,), check subsets of current line
    with open(input_file, 'r') as file:
        sets = [line.strip().split(',') for line in file.readlines()]

    edges = find_edges(sets) # subsets found, starting subset check from lowest/least element first to largest element
    write_edges_to_file(edges, output_file)


# Example main

# set file vars
input_file = "input.txt"
output_file = "output.txt"

# create G with example input from project pdf
print("\nCreating graph G(" + input_file + ") --> " + output_file + " ...")

create_graph(input_file, output_file) # takes input_file data --(computes subsets)--> writes subset data in output_file. Order: increasing of compared elem i (left side)

print("done.")
