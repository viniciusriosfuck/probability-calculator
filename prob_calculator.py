import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.hat = kwargs
        self.contents = []
        
        self.get_contents()
        
    # def __str__(self):
    #     pass
    
    # def __repr__(self):
    #     pass 
    
    def get_contents(self):
        self.contents = []
        for k,v in self.hat.items():
            for _ in range(v):
                self.contents.append(k)
            
    def draw(self, num_balls_drawn):
        if num_balls_drawn > len(self.contents):
            self.get_contents()
            return self.contents
        else:
            samples = random.sample(self.contents, num_balls_drawn)
            for sample in samples:
                self.contents.remove(sample)
            return samples


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    """ Monte Carlo simulation

    Args:
        hat (Hat): A hat object containing balls 
            that should be copied inside the function.
        expected_balls (dict): An object indicating the exact group of balls 
            to attempt to draw from the hat for the experiment.
            For example, to determine the probability of drawing
            2 blue balls and 1 red ball from the hat,
            set expected_balls to {"blue":2, "red":1}.
        num_balls_drawn (int): The number of balls to draw out of the hat
            in each experiment.
        num_experiments (int): The number of experiments to perform. 
            (The more experiments performed, the more accurate 
            the approximate probability will be.)
    Returns:
        float: probability
    """
    match = 0   
    for _ in range(num_experiments):
        experiment_colors = hat.draw(num_balls_drawn)
        experiment_count_colors = {color: experiment_colors.count(color)
                                   for color in set(experiment_colors)}
        if all(expected_balls[color] <= experiment_count_colors.get(color, 0)
               for color in expected_balls.keys()):
            match += 1
        
        # restart contents to hat items
        hat.get_contents()
    
    return match / num_experiments    
