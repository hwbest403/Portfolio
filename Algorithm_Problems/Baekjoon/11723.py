import sys
input = sys.stdin.readline

class sset:
    def __init__(self):
        self.S = set()

    def command(self, com, material):
        if com == 'add':
            self.S.add(material)
        if com == 'remove':
            if material in list(self.S):
                self.S.remove(material)
        if com == 'check':
            if material in list(self.S):
                print(1)
            else:
                print(0)
        if com == 'toggle':
            if material in list(self.S):
                self.command('remove', material)
            else:
                self.command('add', material)
        if com == 'all':
            self.S = set(i for i in range(1, 21))
        if com == 'empty':
            self.S = set()


s = sset()
for _ in range(int(input())):
    command = list(input().split())
    if len(command) == 1:
        command.append(None)
    else:
        command[1] = int(command[1])
    s.command(command[0], command[1])