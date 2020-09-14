#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # build the dict with source as keys and destinations as values
    d = {}
    for i in range(len(tickets)):
        d[tickets[i].source] = tickets[i].destination

    # build the output list terminating in "NONE"
    #find destination for key in d that is none 
    dest = d["NONE"]
    route = [dest]
    
    while dest != "NONE":
        # use the dest as a source
        dest = d[dest]
        route.append(dest)

    return route
