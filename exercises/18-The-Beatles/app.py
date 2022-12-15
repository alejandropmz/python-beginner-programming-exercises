# Your code here!!

def sing():
    song=""
    for i in range(1,13):
        if i == 5:
            song+= "whisper words of wisdom, "
        elif i == 11:
            song+= "there will be an answer, "
        elif i == 12:
            song+= "let it be"
        else:
            song+= "let it be, "
        
    return song

print(sing())