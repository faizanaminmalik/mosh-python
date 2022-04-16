#Stack is LIFO

browsing_history = []
browsing_history.append(1)
browsing_history.append(2)
print (browsing_history)
browsing_history.pop()
browsing_history.pop()
if not browsing_history:
    print("Disable back button")