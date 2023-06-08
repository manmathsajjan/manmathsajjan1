class Set:
    def __init__(self):
        self.elements = []

    def add(self, newElement):
        if newElement not in self.elements:
            self.elements.append(newElement)

    def remove(self, element):
        if element in self.elements:
            self.elements.remove(element)

    def contains(self, element):
        return element in self.elements

    def size(self):
        return len(self.elements)

    def iterator(self):
        return iter(self.elements)

    def intersection(self, otherSet):
        intersectionSet = Set()
        for element in self.elements:
            if otherSet.contains(element):
                intersectionSet.add(element)
        return intersectionSet

    def union(self, otherSet):
        unionSet = Set()
        unionSet.elements = self.elements.copy()
        for element in otherSet.elements:
            unionSet.add(element)
        return unionSet

    def difference(self, otherSet):
        differenceSet = Set()
        for element in self.elements:
            if not otherSet.contains(element):
                differenceSet.add(element)
        return differenceSet

    def subset(self, otherSet):
        for element in self.elements:
            if not otherSet.contains(element):
                return False
        return True


# Example usage
set1 = Set()
set1.add(1)
set1.add(2)
set1.add(3)

set2 = Set()
set2.add(3)
set2.add(4)
set2.add(5)

print("Set 1:", list(set1.iterator()))
print("Set 2:", list(set2.iterator()))

print("Intersection:", list(set1.intersection(set2).iterator()))
print("Union:", list(set1.union(set2).iterator()))
print("Difference (Set 1 - Set 2):", list(set1.difference(set2).iterator()))

print("Set 1 is a subset of Set 2:", set1.subset(set2))
