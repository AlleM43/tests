def Judger(path): # broken. completely broken.
    result = "dat glitch tho"
    if path == "pacifist" or "Pacifist":
        result = "i am nice. i am sans."
    elif path == "neutral" or "normal" or "Neutral" or "Normal":
        result = "You Will Be Judged"
    elif path == "genocide" or "Genocide":
        result = "GET DUNKED ON MO**********"
    else:
        result=path + "Is not a valid path"
    return(result)
print(Judger(""))
