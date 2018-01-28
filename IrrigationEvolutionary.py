# Evolution of irrigation

# Import libraries
import numpy as np
import matplotlib.pyplot as plt
import random
import pandas as pd

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
                pass
        
        for i in range(self.number_of_sprinklers):
            turn_on_sprinkler(self)
        return self.field, self.sprinkler_coords
        
    def score(self):
        '''
        Returns the score of the layout, which is simply the sum of the matrix
        '''
        return -np.sum(self.field)
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
        '''
        Generates a population of by default size 50.
        '''
        self.population_size = population_size
        self.population = pd.DataFrame(columns=['sprinkler_species', 'score', 'sprinker_coords'], index=[x for x in range(self.population_size)])
        for i in range(population_size):
            self.sprinkler_species, self.sprinkler_coords_for_species = self.add_sprinklers()
            self.score_for_layout = self.score()
            self.population['sprinkler_species'][i] = self.sprinkler_species
            self.population['score'][i] = self.score_for_layout
            self.population['sprinker_coords'][i] = self.sprinkler_coords_for_species
            self.field = np.zeros(self.input_size)
        return self.population
        
    def rank_population(self):
        '''
        Ranks the population by score.
        '''
        self.population = self.population.sort_values(by='score', ascending=False)
        self.population = self.population.reset_index()
        return self.population
        
    def select_from_population(self, best_sample_count=10, lucky_few_count=5):
        '''
        Selects the top best_sample_count species and picks lucky_few_count outside of the
        top species.
        '''
        self.best_sample_count = best_sample_count
        self.lucky_few_count = lucky_few_count
        self.next_generation = pd.DataFrame(columns=['index', 'sprinkler_species', 'score', 'sprinkler_coords'], index=[x for x in range(self.population_size)])
        self.next_generation.iloc[:self.best_sample_count] = self.population[:self.best_sample_count]
        self.next_generation[self.best_sample_count:] = self.population[self.best_sample_count:].sample(self.lucky_few_count)
        self.population = self.next_generation
        return self.population
        
    def create_child(self, parent1, parent2):
        self.child = []
        self.parent1 = parent1
        self.parent2 = parent2
        for i, coord in enumerate(self.parent1):
            self.child.append((int(coord[0] + self.parent2[i][0] / 2), int(coord[1] + self.parent2[i][1])))
        return self.child
        

                
        
    def __str__(self):
        return str(self.field)
        
x = irrigation_field()
x.add_sprinklers(sprinkler_cost=4)
print(x.score())
#print(x)
x.display_field_as_image()
x.generate_population()
x.rank_population()
z = x.select_from_population()
y = x.create_child(z['sprinkler_coords'][1], z['sprinkler_coords'][2])
