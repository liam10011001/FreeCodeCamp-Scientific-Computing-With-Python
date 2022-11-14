import copy
import random
# Consider using the modules imported above.

class Hat:

    def __init__(self, **balls):
        self.contents = list()
        for (color, numb) in balls.items():
            for i in range(numb):
                self.contents.append(color)

    def draw(self, num_of_balls):
        drawn = list()
        if num_of_balls > len(self.contents):
            drawn = copy.deepcopy(self.contents)
            self.contents.clear()
        else:
            for i in range(num_of_balls):
                index = random.randint(0, len(self.contents)-1)
                ball = self.contents.pop(index)
                drawn.append(ball)
        return drawn
    
    def __str__(self):
        return str(self.contents)

def expectedOutcome(outcome, expected_balls):
    # count the ball according to the number of occurence of each color

    for (color, occurence) in expected_balls.items():
        count = occurence
        for ball in outcome:
            if count == 0:
                break
            if ball == color:
                count -= 1
        if count > 0: # there is no enough ball for the current color
            return False

    return True



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    num_occurence = 0
    for i in range(num_experiments):
        copy_hat = copy.deepcopy(hat)
        outcome = copy_hat.draw(num_balls_drawn)
        if expectedOutcome(outcome, expected_balls):
            num_occurence += 1
    prob = num_occurence / num_experiments     
    return round(prob, 3)

if __name__ == "__main__":
    hat = Hat(blue=3,red=2,green=6)
    expected = {"blue":2,"green":1}
    num_balls_drawn = 4
    num_experiments = 1000

    print("Balls :", hat)
    print("Expected Outcome :", expected)
    print("Number of balls to be drawn at a time :", num_balls_drawn)
    print("Number of experiments :", num_experiments)
    for i in range(10):
        probability = experiment(hat, expected, num_balls_drawn, num_experiments)
        print("Test ", i+1, "\t:\t", probability)
