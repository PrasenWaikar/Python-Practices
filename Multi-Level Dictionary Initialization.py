from collections import defaultdict
tree = lambda: defaultdict(tree)
nested_dict = tree()
nested_dict['level1']['level2']['level3'] = 'end'
