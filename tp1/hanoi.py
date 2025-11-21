def hanoi(n:int, org:Tower='A',
                 dst: Tower='C',
                 aux: Tower= 'B') -> list[Move]:
    if n == 1:
        