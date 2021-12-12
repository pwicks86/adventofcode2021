from collections import defaultdict
with open("input.txt", "r") as f:
    lines = f.read().splitlines()

cave_map = defaultdict(set)

for l in lines:
    from_cave, to_cave = l.split("-")
    cave_map[from_cave].add(to_cave)
    cave_map[to_cave].add(from_cave)

class Path:
    def __init__(self):
        self.visited_small = set()
        self.path = []

    def add_part(self, part):
        if part.islower():
            self.visited_small.add(part)
        self.path.append(part)

    def is_complete(self):
        return self.path[-1] == "end"

    def get_neighbors(self):
        last_part = self.path[-1]
        n =[]
        for neighbor in cave_map[last_part]:
            if neighbor not in self.visited_small:
                p = Path()
                p.path = list(self.path)
                p.visited_small = set(self.visited_small)
                p.add_part(neighbor)
                n.append(p)
        return n

    def __repr__(self):
        return f"visited: {self.visited_small}, path: {self.path}"

p = Path()
p.add_part("start")
paths = [p]
complete = []
while len(paths) > 0:
    path = paths.pop()
    if path.is_complete():
        complete.append(path)
    else:
        new_paths = path.get_neighbors()
        paths.extend(new_paths)

print(len(complete))

