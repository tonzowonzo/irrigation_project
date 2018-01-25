# Evolution of irrigation

# Import libraries
import numpy as np
import matplotlib.pyplot as plt
import random

class irrigation_field():
    '''
    Creates a field which can then have sprinklers added to it that will water the
    area surrounding them. Sprinklers cost 'money' and the area they water is 
    'beneficial', summing them gives a score which we want to try and maximise
    with an evolutional algorithm.
    '''
    
    
    def __init__(self, input_size=(16, 16), number_of_sprinklers=12):
        self.input_size = input_size
        self.number_of_sprinklers = number_of_sprinklers
        self.field = np.zeros(input_size)
    
    def add_sprinklers(self, sprinkler_cost=2, sprinkler_range=2, water_benefit=-0.5):
        '''
        Function to add sprinklers to the field.
        '''
        self.sprinkler_range = sprinkler_range
        self.sprinkler_x = [random.randint(self.sprinkler_range, self.input_size[1] - self.sprinkler_range) for x in range(self.number_of_sprinklers)]
        self.sprinkler_y = [random.randint(self.sprinkler_range, self.input_size[1] - self.sprinkler_range) for x in range(self.number_of_sprinklers)]
        self.sprinkler_coords = list(zip(self.sprinkler_y, self.sprinkler_x))
        self.sprinkler_cost = sprinkler_cost
        self.water_benefit = water_benefit
        
        def turn_on_sprinkler(self):
            '''
            Adds the surrounding water to a sprinkler.
            '''
            try:
                self.field[self.sprinkler_coords[i][0]][self.sprinkler_coords[i][1]] = self.sprinkler_cost # Places a sprinkler.
                for j in range(self.sprinkler_coords[i][0]-self.sprinkler_range, self.sprinkler_coords[i][0]+self.sprinkler_range+1):
                    for k in range(self.sprinkler_coords[i][1]-self.sprinkler_range, self.sprinkler_coords[i][1]+self.sprinkler_range+1):
                        if self.field[j][k] > self.water_benefit and self.field[j][k] != self.sprinkler_cost - 0.5:
                            self.field[j][k] = self.field[j][k] + self.water_benefit
            except IndexError:
                print('List index was out of range')
        
        for i in range(self.number_of_sprinklers):
            turn_on_sprinkler(self)
        return self.field
        
    def score(self):
        '''
        Returns the score of the layout, which is simply the sum of the matrix
        '''
        return np.sum(self.field)
##   We'll ignore the pipes for now
#    def add_pipe(self, pipe_cost=1):
#        self.pipe_x = 0
#        self.pipe_y = 2
#        self.pipe_cost = pipe_cost
#        self.field[self.pipe_y][self.pipe_x] = self.pipe_cost
     
    def display_field_as_image(self):
        '''
        Displays the field being irrigated as an image
        '''
        plt.imshow(self.field)
        plt.tick_params(axis='both', labelbottom='off', labelleft='off')
        plt.show()
        
    def generate_population(self, population_size=50):
        self.population_size = population_size
        self.population = []
        for _ in range(population_size):
            self.sprinkler_species = self.add_sprinklers()
            self.score_for_layout = self.score()
            self.population.append([self.sprinkler_species, self.score_for_layout])
            self.field = np.zeros(self.input_size)
        return self.population
                
        
    def __str__(self):
        return str(self.field)
        
x = irrigation_field()
x.add_sprinklers(sprinkler_cost=4)
print(x.score())
#print(x)
x.display_field_as_image()
x = x.generate_population()