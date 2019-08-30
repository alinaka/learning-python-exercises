import json


class EmptyRemover:
    removed_lists = 0
    removed_dicts = 0

    def remove_empty(self, data):
        if isinstance(data, list):
            if data == []:
                self.removed_lists += 1
                return  self.removed_dicts, self.removed_lists
            data[:]
            for i in data:
                self.remove_empty(i)
        if isinstance(data, dict):
            for i in data:
                self.remove_empty(data[i])
                if not data[i]:
                    del data[i]
                    self.removed_dicts += 1
            if data == {}:
                del data
                self.removed_dicts += 1
        return data, self.removed_dicts, self.removed_lists


def test():
    # data = [[{}], {}, ""]
    # remover = EmptyRemover()
    # answer = remover.remove_empty(data)
    # assert  answer == (2, 1)
    data = [[[]]]
    remover = EmptyRemover()
    answer = remover.remove_empty(data)
    assert answer == (0, 3)
    data = ["", [""], {"": ""}]
    remover = EmptyRemover()
    assert remover.remove_empty(data) == (0, 0)
    data = [{"1": {}, "2": []}]
    remover = EmptyRemover()
    assert remover.remove_empty(data) == (2, 2)


def main():
    with open("input.txt") as file:
        data = json.loads(file.read())
    remover = EmptyRemover()
    with open("ountput.txt", "w") as file:
        file.write(" ".join(map(str, remover.remove_empty(data))))


if __name__ == "__main__":
    test()
