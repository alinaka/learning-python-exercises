import sys

d = {
    'global': {
        'parent': None,
        'vars': []
    }
}


def add(namespace, var):
    if namespace in d:
        d[namespace]['vars'].append(var)


def create(namespace, parent):
    d[namespace] = {
        'parent': parent,
        'vars': []
    }


def get(namespace, var):
    if namespace in d and var in d[namespace]['vars']:
        return namespace
    elif namespace in d and var not in d[namespace]['vars']:
        return get(d[namespace]['parent'], var)
    else:
        return None


def get_namespace_parent(child):
    return d['parent'] if child in d else None


def main():
    n = int(sys.stdin.readline().strip())
    for i in range(n):
        cmd, namesp, arg = sys.stdin.readline().strip().split()
        if cmd == 'add':
            add(namesp, arg)
        elif cmd == 'create':
            create(namesp, arg)
        elif cmd == 'get':
            print(get(namesp, arg))


if __name__ == "__main__":
    main()
