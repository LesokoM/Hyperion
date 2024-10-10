event_times = []
event_list = [ "swimming", "cycling", "running"]





for i in range(0,len(event_list)):
    event_times.append(int(input(f"Please enter the time (in minutes) for {event_list[i]}:")))
    
total_time = sum(event_times)
print("Time taken to complete is:" , total_time)

qualifiying_time = 100

if total_time > qualifiying_time+10:
    print("No Reward")
elif total_time < qualifiying_time+10 and total_time > qualifiying_time+5:
    print("Provincial Scroll")
elif total_time <= qualifiying_time+5 and total_time > qualifiying_time:
    print("Provinical Half Colours")
elif total_time <= qualifiying_time:
    print("Provinical Colours")