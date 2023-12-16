def read_highest_scores(file_path):
    # Read the file and store scores in a dictionary
    scores = {}
    with open(file_path, 'r') as file:
        for line in file:
            name, score = line.strip().rsplit(' ', 1)
            scores[name] = int(score)

    # Sort scores in descending order and retrieve the top 5
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:5]

    # Print the top 5 scores
    for name, score in sorted_scores:
        print(f"{name}: {score}")

# Provide the file path here
file_path = 'Highscores.txt'
read_highest_scores(file_path)
