import random
import re
stories=["Today, I went to the park and saw a {adjective 1} {noun1}. It was {verb1} {adverb1} by the {place1}. I couldn't believe my {body part1}!",\
         "There once was a superhero named {name 1}. Every day, they would {verb} {adverb} to save the {noun} from {villain}. Everyone in the {place} loved {name 2}.",\
         "One day, I decided to cook a {adjective} meal. I took out a {noun 1} and started to {verb}. Suddenly, the {noun 2} exploded {adverb} and covered the entire {place} in {substance}.",\
         "Last weekend, I visited the zoo. The first animal I saw was a {adjective 1} {animal 1} {verb} {adverb}. Then, I saw a {color} {animal 2} eating {food}. It was a {adjective 2} day at the zoo!",\
         "In a {place}, there was a {adjective 1} witch who made a magic potion. She added a {noun 1}, a {adjective 2} {noun 2}, and a drop of {liquid}. After {verb} {adverb}, the potion turned {color} and smelled like {food}."]
def extractplaceholders(story):
    templist=re.findall(r'\{(.*?)\}', story)
    return templist
def userinput(n):
    temp={}
    for i in n:
        temp[i]=input("Enter a "+i+" :")
    return temp
def replacesets(sets,story):
    for key,value in sets.items():
        story=story.replace(f'{{{key}}}', value)
    return story
def play():
    story=random.choice(stories)
    placeholders=extractplaceholders(story)
    sets=userinput(placeholders)
    story=replacesets(sets,story)
    return story
print(play())
