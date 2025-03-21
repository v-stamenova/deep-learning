import numpy as np

w1 = 1
w2 = 1
b = 0

data = []
for i in range(1000):
    input = np.random.randint(low=-100, high=100, size=2)
    data.append({'x1': input[0], 'x2': input[1], 'y': (input[0] + input[1])})

for datum in data:
    x1 = datum['x1']
    x2 = datum['x2']
    y = datum['y']

    y_pred = (w1 * x1) + (w2 * x2) + b
    print(f"Input: ({x1}, {x2}), Predicted Sum: {y_pred}")