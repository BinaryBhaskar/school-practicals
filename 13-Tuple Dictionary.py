def tuples_dict(tuples_list):
    return dict(tuples_list)

all_tuples = [('A', 1), ('B', 2), ('C', 3)]
final_dict = tuples_dict(all_tuples)
print(final_dict)