
def list_mean(L):



    s=0
    length=0

    for l in L:
        if isinstance(l,float):
            s += l
            length += 1

        else:
            if isinstance(l,int):
                s += l
                length += 1
            else:
                print('Unsupported value in list.')
                continue

    return s/length

    def list_stdev(L):
        if L is None:
            return None

        if len(L) == 0:
            return None
