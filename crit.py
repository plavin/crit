import sys
import bgqshared
import contextlib
import ast

offset = (-2,1,0,1,2) 

class DummyFile(object):
    def write(self, x): pass

@contextlib.contextmanager
def nostdout():
    save_stdout = sys.stdout
    sys.stdout = DummyFile()
    yield
    sys.stdout = save_stdout

#path_len will be a measure of how conclicted the path is
#(using that third number in the conflict links tuple)
def path_len(path, conflictlinks):
    length = 0
    for i in range(len(conflictlinks)):
        if conflictlinks[i][0] in path:
            length += conflictlinks[i][1]
    return length

#create path from pt1 to pt2
def path(pt1, pt2):
    l1 = list()
    l1.append(pt1)
    l1.append(pt2)
    p = bgqshared.determineLinkSetPatrick(l1)
    return p

def main(comm1,comm2):
    conflict_dict = []
    
    with nostdout():
        conflict_dict = bgqshared.main(comm1,comm2,1)

    comm1_points = bgqshared.readNodeSet(comm1)


    max_len = 0
    max_path = []
    endpoints = ()
    #measure each point to point distance
    for x in comm1_points:
        if x[4] == 1:
            continue
        for a in offset:
            for b in offset:
                for c in offset:
                    for d in offset:
                        x_prime = (x[0]+a,x[1]+b,x[2]+c,x[3]+d,0)
                        if x_prime in comm1_points:
                            p = path(x, x_prime)
                            l = path_len(p,conflict_dict)
                            if l > max_len:
                                max_len = l
                                max_path = p
                                endpoints = (x,x_prime)

#    print endpoints
#    print max_path
    print "{}".format(max_len)

if __name__ == "__main__":
    sys.exit(main(sys.argv[1],sys.argv[2]))
