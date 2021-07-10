def Toh(n, source, destination, auxiliary):
    if n == 1:
        print("Move disk 1 from source", source, "to destination", destination)
        return
    else:
        Toh(n - 1, source, auxiliary, destination)
        print("Move disk", n, "from source", source, "to destination", destination)
        Toh(n - 1, auxiliary, destination, source)


n = 3
Toh(n, 'A', 'B', 'C')