#working

def hello(curState, string, edges, accept):

    print "curState: ", curState, " string: ", string;
    if(string == ""):
        return curState in accept;


    if((curState, string[0]) in edges):

        dest = edges[(curState, string[0])];

        for newCurState in dest:
            return hello(newCurState, string[1:], edges, accept);

    elif((curState, '') in edges):

        dest = edges[(curState, '')];

        for newCurState in dest:
            return hello(newCurState, string, edges, accept);

    else:
        return False;


edges = {(1,'a'):[4,2], (2,'b'):[3],  (4,''):[5], (3,'c'):[3], (5,'b'):[3], (5,'c'):[6], (5,''):[6]};

accept = [3,6];

string = "abc";

print hello(1, string, edges, accept);