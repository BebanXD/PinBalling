def read_highest_scores(): #reads out top 5 highscores
    output =[]
    scores = {}
    with open('Highscores.txt', 'r') as file:
        for line in file:
            name, score = line.strip().rsplit(' ', 1)
            scores[name] = int(score)
    
    # Sort
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    
    # return the top 5 scores
    for name, score in sorted_scores[:5]:
        output.append([name,score])
    return output

def selection(input,length):
    return input % length 
    
#def radness_handler(level): #input levels from 0 to 5
    #sound

    #text 1
    #screen.blit(text,(t/50,30*np.sin(t/600)))

    #image 1 


    #image 2

    #hyper mode
        

