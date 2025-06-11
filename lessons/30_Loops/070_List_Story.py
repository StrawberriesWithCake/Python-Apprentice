"""
Use the words in the list to create a story. 

Use indexing to get words from the list, then 
append them to the story

"""

words = ['Once', '👦', 'upon', '🐕', 'park', 'met', 'with', 'a', 'the', 
    'time', 'to', 'who', '🐈', '👧', 'and', 'went', 'had', 'play', '⚽.', 'they']

story = []
story.append(words[0:3:2])
story.append(words[7:9:9])
story.append(words[7])
story.append(words[1])
story.append(words[15])
story.append(words[10])
story.append(words[8])
story.append(words[4])
story.append(words[14])
story.append(words[5])
story.append(words[12:14])
story.append(words[11])
story.append(words[15])
story.append(words[10])
story.append(words[17:19])

# Create a story using the words in the list

# Display the story to the user
for i in story:
    print(i)