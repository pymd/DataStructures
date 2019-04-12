total_steps = 0

def make_move(from_tower,to_tower,ele):
    global total_steps
    total_steps += 1
    print 'Moving element:',ele,'from',towers[id(from_tower)],'to',towers[id(to_tower)]
    to_tower.insert(0,ele)


def solveTowersOfHanoi (n, source, aux, dest):
    global total_steps
    if n == 0:
        return
    if n == 1:
        to_move = source.pop(0)
        make_move(source,dest,to_move)              # only 1 element in source => move to dest
        return

    remaining = source.pop(n-1)                     # save the highest element of source
    solveTowersOfHanoi (n-1,source,dest,aux)        # recursively move all top source elements to aux using dest as auxiliary

    make_move(source,dest,remaining)                # make the actual move

    solveTowersOfHanoi (n-1,aux,source,dest)        # recursively move all aux elements to dest using source as auxiliary

if __name__ == '__main__':
    n = input('Please enter a value for n:')
    print 'Solving for n =',n

    source = range(1,n+1)
    dest = list()
    aux = list()

    towers = {id(source):'source',id(dest):'dest',id(aux):'aux'}

    print 'Initially:'
    print 'Source:',source
    print 'Dest:',dest
    print 'Aux:',aux

    solveTowersOfHanoi (n,source,aux,dest)

    print 'Eventually:'
    print 'Source:',source
    print 'Dest:',dest
    print 'Aux:',aux

    print 'Total steps taken = ',total_steps
