from flask import Flask
import random

app = Flask(__name__)

number = random.randint(0, 9)
colors = ['#ffbbb', '#8d6c9f', '#638652', '#36476f', '#3e868e', '#d1b896', '#6f6f6f', '#d3a625']
too_low_img = ['https://media.giphy.com/media/w87yLYL7lwDWE/giphy.gif',
               'https://media.giphy.com/media/pHt6eQrQyok8w/giphy.gif',
               'https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif',
               'https://media.giphy.com/media/3ohhwo81vLfGfDsDrG/giphy.gif']
too_high_img = ['https://media.giphy.com/media/VWwS82FgMKRm8/giphy.gif',
                'https://media.giphy.com/media/8s6n9sZfH8i3K/giphy.gif',
                'https://media.giphy.com/media/aaTz9fnXkzoQ/giphy.gif']
found_img = 'https://media.giphy.com/media/elsol3P5Jt2ASsxLva/giphy.gif'

print(number)
@app.route('/')
def homepage():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/l378khQxt68syiWJy/giphy.gif'>"


@app.route('/<int:num>')
def number_page(num):
    color = random.choice(colors)
    if num > number:
        message = "Too high, try again!"
        image = random.choice(too_high_img)
    elif num < number:
        message = "Too low, try again!"
        image = random.choice(too_low_img)
    else:
        message = "Congratulations! You found the number!"
        image = found_img
    return f"<h1 style='color:{color}'>{message}</h1>" \
           f"<img src={image} width=500>"


# export


if __name__ == "__main__":
    app.run(debug=True)
