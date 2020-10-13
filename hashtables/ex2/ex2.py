class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    # cache
    index = {}
    sorted_tickets = []

    for i in tickets:
        index[i.source] = i.destination
    
    destination = index["NONE"]
    while destination != "NONE":
        sorted_tickets.append(destination)
        destination = index[destination]
    
    sorted_tickets.append("NONE")
    print(index)
    print(sorted_tickets)
    return sorted_tickets
