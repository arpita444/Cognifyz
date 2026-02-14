with open ("filemanipulation.txt","w") as f:
    f.write("India, officially the Republic of India, is the world's largest democracy and the seventh-largest country by area, known for its ancient civilization, rich cultural diversity, and varied geography, from Himalayan peaks to tropical coasts, serving as a hub for various religions, languages, and cuisines. It's a Sovereign, Secular, Democratic Republic, governed by a parliamentary system, with a capital in New Delhi, and comprises 28 states and 8 union territories. ")
with open("filemanipulation.txt","r") as f:
    word_count=0
    file_content=f.read()
    word_count=file_content.split()
    word_count=len(word_count)
    print(word_count)