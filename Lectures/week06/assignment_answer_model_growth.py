import sys
import numpy as np

def main():

    filename = sys.argv[1]
    rate_params = sys.argv[2:]


    range_rate = np.arange(float(rate_params[0]), float(rate_params[1]), float(rate_params[2]))
    experiment_data = np.loadtxt(filename, delimiter=',')

    # define a function that calcualates mean squared error
    def squared_error(prediction, data):
        residual = prediction - data
        mse = (residual**2).mean()
        return mse

    # try the parameters and choose the one with the least squared error
    mse = []
    N0 = experiment_data[0]
    t = np.linspace(0, 10, len(experiment_data))
    for r in range_rate:
        prediction = N0*np.exp(r*t)
        mse.append(squared_error(prediction, experiment_data))

    best_fit = range_rate[np.argmin(mse)]
    print('We predict the rate of growth of this bacterial population to be', best_fit)


if __name__ == '__main__':
   main()


## Part 2 answers
# git add model_growth.py
# git commit -m "message"
# git push origin master
