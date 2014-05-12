class Node:
  def __init__(self, id, label):
    self.id = id
    self.label = label
    self.neighbours = []

  def __str__(self):
    return "({}: {})".format(self.id, self.label)

  def add_neighbour(self, neighbour, label):
    self.neighbours.append((neighbour, label))

  def get_neighbours(self, label):
    if not label:
        return [x[0] for x in self.neighbours]
    return [x[0] for x in self.neighbours if label == x[1]]

  def degree(self, label):
    if not label:
        return len(self.neighbours)
    total = 0
    for x in self.neighbours:
        if x[1] == label:
            total += 1
    return total

  def has_neighbour(self, node, label):
    for x in self.neighbours:
        if x[0] == node:
            if label:
                if x[1] == label:
                    return True
                else:
                    return False
            return True
    return False