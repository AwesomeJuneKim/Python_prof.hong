import pizza
pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(17,'mushrooms', 'green peppers', 'extra cheese')

from pizza import make_pizza
make_pizza(16, 'pepperoni')

from pizza import make_pizza as mp
mp(16, 'pepperoni')