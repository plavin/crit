import sys
import bgqshared
import contextlib

offset = (-2,0,2) 

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
    len = 0
    return len

#create path from pt1 to pt2
def path(pt1, pt2):
    p = []
    return p

#get nodes in a communicator and put in a list
def readNodeSet(file):
  list = []
  with open(file) as f:
    for line in f.readlines():
      list.append(ast.literal_eval(line))
  return list

def main(comm1,comm2):
    conflict_dict = []
    with nostdout():
        #get conflicted links
        conflict_dict = bgqshared.main(comm1,comm2,1)

    comm1_points = readNodeSet(comm1)

    max_len = 0
    max_path = []
    #measure each point to point distance
    for x in comm1_points:
        for a in offset:
            for b in offset:
                for c in offset:
                    for d in offset:
                        x_prime = (x[0]+a,x[1]+b,x[2]+c,x[3]+d,0)
                        if (x_prime in comm1_points): #pseudo code
                            p = path(x, x_prime)
                            if path_len(p) > max_len:
                                max_len = path_len(p, conflictlinks)
                                max_path = p
                            

if __name__ == "__main__":
    sys.exit(main(sys.argv[1],sys.argv[2]))
