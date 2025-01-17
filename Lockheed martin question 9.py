"""
1
4
A1,Code Questers,Day,E1,true
A2,Maintenance,Day,E1,false
A3,LM Peeps,Night,E1,true
A4,Code Questers,Day,E2,true
"""
def process():
    record_number = int(input())

    events = {}
    for i in range(record_number):
        ID, name, session, event_ID, participation = input().split(",")
        #name = name.replace(" ", "")
        if participation == "false":
            continue
        if session == "Night":
            i = 1
        else:
            i = 0
        if event_ID in events.keys():
            events[event_ID][i] += 1
        else:
            events[event_ID] = {}
            events[event_ID][0] = 0
            events[event_ID][1] = 0
            events[event_ID][i] = 1
    i = 1
    for key, val in events.items():
        sentence = key + "," + str(val[0])+ ","+ str(val[1])
        sentence = sentence.replace(" ", "")
        print(sentence)
        i += 1
    

num_trials = int(input())
for num in range(num_trials):
    process()
