import sys

classes = {}


def is_another_class(ancestor, child):
    if classes[child]["parents"]:
        for parent in classes[child]["parents"]:
            return is_an_ancestor_of(ancestor, parent)
    return False


def is_an_ancestor_of(class1, class2):
        if class1 == class2:
            if class1 not in classes or class2 not in classes:
                return False
            else:
                return True
        elif class1 in classes[class2]['parents']:
            return True
        elif is_another_class(class1, class2):
            return True
        else:
            return False


def main():
    n = int(sys.stdin.readline().strip())

    for i in range(n):
        class_name = sys.stdin.readline().strip()
        if " : " not in class_name:
            parents = []
        else:
            class_name, parents = class_name.split(" : ")
            parents = parents.split()
        classes[class_name] = {
            "parents": parents
        }
    q = int(sys.stdin.readline().strip())
    compare = [sys.stdin.readline().strip().split() for _ in range(q)]
    for parent, child in compare:
        result = is_an_ancestor_of(parent, child)
        result = "Yes" if result else "No"
        print(result)


if __name__ == "__main__":
    main()
