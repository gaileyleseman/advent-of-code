from anytree import NodeMixin, RenderTree, PreOrderIter

class Directory(NodeMixin):
    def __init__(self, name, parent=None, children=None):
        self.name = name
        self.parent = parent
        self.files = []
        if children:
            self.children = children

    def __repr__(self):
        return self.name
    
    def add_file(self, file_size):
        self.files.append(file_size)

    def get_size(self):
        total_size = sum(self.files)
        for child in self.children:
            total_size += child.get_size()
        return total_size


def parse_text(input_txt):
    with open(input_txt, "r") as f:
        lines = f.read().split('\n')
        data, command_set = [], []
        for line in lines:
            if line[0:4] == "$ cd" and len(command_set)>0:
                data.append(command_set)
                command_set = []
            command_set.append(line)
        data.append(command_set)
    return data


def cd(command, current_directory):
    prompt, cd, new_directory = command.split(" ")
    if new_directory == "..":
        return current_directory.parent
    if new_directory == "/":
        return current_directory.root
    for child in current_directory.children:
        if new_directory == child.name:
            return child


def create_directory_tree(data):
    current_directory = Directory("/")
    for command_set in data:
        current_directory = cd(command_set[0], current_directory)
        for command in command_set[1:]:
            x, name = command.split(" ")
            if x.isnumeric():
                current_directory.add_file(int(x))
            if x == "dir":
                new_directory = Directory(name, parent=current_directory)
    
    return current_directory.root


def print_tree(tree):
    for pre, _, node in RenderTree(tree):
        treestr = u"%s%s" % (pre, node.name)
        print(treestr.ljust(8), node.get_size())


def part1(data):  
    tree = create_directory_tree(data)
    # print_tree(tree)
    sizes = [directory.get_size() for directory in PreOrderIter(tree) if directory.get_size() < 100000]
    return sum(sizes)


def part2(data):
    tree = create_directory_tree(data)
    required_space = 30000000 - (70000000 - tree.root.get_size())
    sizes = [directory.get_size() for directory in PreOrderIter(tree) if directory.get_size() > required_space]
    return min(sizes)


if __name__ == '__main__':
    test_data = parse_text("test.txt")
    input_data = parse_text("input.txt")

    print("TEST: Part 1: ", part1(test_data))
    print("Part 1: ", part1(input_data))

    print("TEST: Part 2: ", part2(test_data))
    print("Part 2: ", part2(input_data))
