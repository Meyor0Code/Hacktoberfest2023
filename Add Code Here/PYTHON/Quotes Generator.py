import random

# List of quotes
quotes = [
    "You must be the change you wish to see in the world.",
    "The greatest glory in living lies not in never falling, but in rising every time we fall.",
    "The way to get started is to quit talking and begin doing.",
    "If you look at what you have in life, you'll always have more. If you look at what you don't have in life, you'll never have enough.",
    "You may say I'm a dreamer, but I'm not the only one. I hope someday you'll join us. And the world will live as one.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts.",
    "The only limit to our realization of tomorrow will be our doubts of today.",
    "Don't watch the clock; do what it does. Keep going.",
    "It's not whether you get knocked down, it's whether you get up.",
    "The future belongs to those who believe in the beauty of their dreams."
]

# Function to get a random quote
def get_random_quote(quotes):
    return random.choice(quotes)

if __name__ == '__main__':
    # Get and print a random quote
    random_quote = get_random_quote(quotes)
    print(random_quote)
