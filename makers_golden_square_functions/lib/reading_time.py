import math 
def reading_time(str):
    if not str:
        raise Exception("No text to be read.")
 
    
    seconds = math.ceil(0.3* len(str.split()))
    mod_seconds = seconds % 60
    minutes = int((seconds - mod_seconds) / 60)
   
    print(seconds)
    print(minutes)
    print(mod_seconds)
    
    return f"Estimated reading time: {minutes} minutes and {mod_seconds} seconds."