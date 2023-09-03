from flask import Flask, render_template, request

app = Flask(__name__)

# Import your chat AI code here
import re
import random

word_actions = {
    "calculate": "perform_calculation",
    "add": "+",
    "subtract": "-",
    "multiply": "*",
    "divide": "/",
    "generate": "generate_text",
    "greet": "Hello! How can I assist you today?",
    "farewell": "Goodbye! Have a great day.",
    "generate text": "generate_text",
    "can you calculate": "perform_calculation",
    
}

# Define grammar actions
generate = {
    "sub": ["The sun", "A gentle breeze", "The smell of freshly baked bread", "A group of friends", "The city skyline", "A child's laughter", "Waves", "The aroma of coffee", "Birds", "A skilled pianist's fingers", "The scent of blooming flowers", "Hikers", "A street performer", "The pages of an old book", "Raindrops", "A chef", "In a bustling market", "Stars", "The soft purring of a cat", "A scientist", "Children", "A painter", "The distant sound of a train whistle", "Friends", "The aroma of a barbecue", "Waves gently lapped", "An orchestra", "The first snowflakes", "A group of activists", "The hum of a busy city", "A baker's hands", "A toddler", "The scent of pine trees", "A photographer", "Friends embarked", "A baby's giggle", "A farmer", "The sound of thunder", "Dancers", "A street artist", "A pilot", "The fragrance of a bouquet of roses", "Children built", "A teacher", "A scientist made", "The crackling of a fireplace", "A comedian", "The rustling of leaves", "A couple", "A poet poured"],
    "act": ["rose over the horizon, casting a warm glow", "rustled the leaves", "wafted through the air, enticing passersby", "gathered around a campfire, sharing stories and laughter", "glittered with a million lights", "echoed through the park", "crashed against the shore, creating a symphony of sounds", "filled the cozy cafe, providing comfort", "chirped merrily in the early morning", "danced across the keys, producing a beautiful melody", "permeated the garden, attracting bees and butterflies", "trekked through the rugged mountains, taking in breathtaking views", "captivated a crowd with their mesmerizing juggling act", "turned slowly", "pitter-pattered on the windowpane, creating a cozy ambiance", "expertly chopped vegetables, preparing a delicious meal", "called out their wares, creating a lively atmosphere", "twinkled in the night sky, inspiring wonder", "provided comfort to its owner", "worked diligently in the lab, conducting experiments", "raced down a hill, their laughter filling the air", "carefully mixed colors on their palette, creating a work of art", "carried on the wind", "gathered around a bonfire, toasting marshmallows", "filled the neighborhood, making mouths water", "gently lapped at the edge", "performed a symphony, moving the audience", "of winter fell softly", "marched through the streets, advocating for change", "faded away", "skillfully shaped dough", "took their first wobbly steps, cheered on", "filled the air", "captured a stunning sunset", "embarked on a road trip, eager", "was infectious, bringing smiles", "tended to their crops, nurturing the land", "rumbled in the distance, announcing an approaching", "twirled and leaped on stage, expressing themselves", "created a masterpiece with colorful chalk", "guided a plane through the clouds, soaring", "filled a room, a gift", "built sandcastles on the beach, their imaginations", "inspired young minds, shaping", "made a groundbreaking discovery, changing", "provided warmth and comfort", "had the audience in stitches", "signaled the changing seasons", "danced under the stars, lost", "poured their heart into words, creating a poem"],
    "tence": ["across the landscape.", "in the forest, creating a soothing melody.", "enticing passersby.", "sharing stories and laughter.", "as night fell.", "as they played on the swings.", "against the shore, creating a symphony of sounds.", "on a rainy day.", "announcing the start of a new day.", "that touched souls.", "a quiet park.", "above the world.", "of love.", "imaginations running wild.", "the future.", "the course of history.", "on a cold night.", "with their witty jokes.", "the changing seasons.", "in each other's arms.", "that touched souls."]
}

# Function to perform calculations
def perform_calculation(expression):
    try:
        result = eval(expression)
        return f"The result is: {result}"
    except Exception as e:
        return f"Error: {str(e)}"

# Function to generate text using grammar actions
def generate_random_text():
    sub = random.choice(generate["sub"])
    act = random.choice(generate["act"])
    tence = random.choice(generate["tence"])
    return f"{sub} {act} {tence}"
    


# Define the functions from your chat AI code here
def chat_ai(input_text):
    input_text = input_text.lower()
    words = re.findall(r'\w+', input_text)
    response = ""

    for word in words:
        if word in word_actions:
            action = word_actions[word]
            if action == "perform_calculation":
                expression = input_text.split(word, 1)[1].strip()
                response = perform_calculation(expression)
            elif action == "generate_text":
                response = generate_random_text()
            else:
                response = action
            break

    return response

@app.route('/')
def index():
    return render_template('index.html', response="")

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    response = chat_ai(user_input)
    return render_template('index.html', response=response,user_input=user_input)

if __name__ == '__main__':
    app.run(debug=True)
