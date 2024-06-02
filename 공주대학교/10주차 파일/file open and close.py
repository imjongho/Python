class open2(object):
    def __init__(self, path, rw):
        print("initialized")
        self.file = open(path)

    def __enter__(self):
        print("entered")
        return self.file

    def __exit__(self, ext, exv, trb):
        print("exited")
        self.file.close()
        return True


with open2('test.txt', 'r') as file:     # path <- 'text.txt'
    str = file.read()
    print(str)
    # file.close() 한거와 같음
