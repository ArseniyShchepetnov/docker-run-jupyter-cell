"""Write hello world to the file."""


def write_helloworld(file):
    with open(file, "w", encoding="UTF-8") as fobj:
        fobj.write("Hello World!")
