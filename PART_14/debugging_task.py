# Function to print dictionary values given the keys
def print_values_of(dictionary, keys): 
    for k in keys: 
        #-----------------------------------
        #we want k found in the our dictionary not key 
        #------------------------------------
        print(dictionary[k])

# Print dictionary values from simpson_catch_phrases
simpson_catch_phrases = {
    "lisa": "BAAAAAART!", 
    "bart": "Eat My Shorts!", 
    "marge": "Mmm~mmmmm", 
    "homer": "d'oh!",
    #------------------------------------------
    #syntax issue with dictionary[homer] fixing the quotatiaion marks
    # -------------------------------------- 
    "maggie": "(Pacifier Suck)"
                         }

#-------------------------------------------------
#since the fucntion only tales 2 arguments we can create 1 list that holds the 
#variables that we want
#---------------------------------------------
character = ["lisa", "bart", "homer"]
print_values_of(simpson_catch_phrases, character)

'''
    Expected console output:

    BAAAAAART!
    Eat My Shorts!
    d'oh!

'''
