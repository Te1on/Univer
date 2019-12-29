class FIFO:
    def __init__ (self, *args):
        self.args = list(args)

    def isEmpty(self):
        if len(self.args) == 0:
            return True
        return False

    def push(self, obj):
        self.args.append(obj)
        print(str(obj) + " was added to queue")

    def pop(self):
        print(str(self.args[0]) + " was pop out from queue")
        return self.args.pop(0)

    def __repr__(self):
        res = ""
        for i in range(len(self.args)):
            res += "#"+str(i + 1) + " " + str(self.args[i])
            if i != len(self.args) - 1:
                res += '\n'
        return res


if __name__ == "__main__":
    ochered = FIFO("Vasya", "Dima", "Vanya")
    print(ochered)
    ochered.push("Boris")
    print(ochered)
    ochered.pop()
    print(ochered)
