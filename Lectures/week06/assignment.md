# Assignment

1) Take the code you wrote in assignment 2 for predicting population growth in bacteria and make it into a command line script.
The goal is to have a code that can read a collected data from a csv file, and our desired range of rates, and returns what it thinks is the best fit:

Our collaborator sends us a csv file named `bacteria.csv`, they have started with a colony of 300 bacteria and have counted the population 100 times in the course of 10 days. We hypothesize that the daily growth has an exponential model and we want to find the rate that bests fit an exponential model to the data. We want a script that takes the csv file, and the range of rates that we desire and returns the best rate. Something like below in the command line:

```bash
python model_growth.py bacteria.csv 0.1 1 0.1
```
we open `atom model_growth.py` and copy our previous code. Fill the lines necessary for making it a command line, the lines for you to fill are named as a) to ..:

```Python
**a) ....**
import numpy as np

def main():

    filename = **b)...**
    rate_params = **c)....**


    range_rate = np.arange(float(rate_params[0]),float(rate_params[1]),float(rate_params[2])) #here we made a slight change: since the parameters that are read by sys library are strings, we have to convert them to floats. If we were using argpars library we could define type = 'float'
    experiment_data = **d)...**

    # define a function that calcualates mean squared error
    def squared_error(prediction,data):
        residual = prediction - data
        mse = (residual**2).mean()          #or np.sum(residual**2)
        return mse

    # try the parameters and choose the one with the least squared error
    mse = []
    # note two modifications below: we are taking the N0 and the time vector from data
    N0 = experiment_data[0]
    t = np.linspace(0,10,len(experiment_data))
    for r in range_rate:
        prediction = N0*np.exp(r*t)
        mse.append(squared_error(prediction,experiment_data))

    best_fit = range_rate[np.argmin(mse)]
    print('We predict the rate of growth of this bacterial population to be',best_fit)

**e)...**
**d)...**
```
save and close.

2) Try your code in command line with a few parameter ranges and report what is the rate you predict for the dataset shared with you.
for example:
```
python model_growth.py bacteria.csv 0 2 0.1
```

3) Fork the class repository, the bacteria.csv data and the model_growth.py files are copied there. change the python script as you did in the first section, and do a pull request to the class repo. The steps you should take are as below if you were not in the tutorial and haven't forked the class repo, if you already have, jump in to step 4:
  1- fork on GitHub
  2- copy the link for cloning
  3- open git terminal in your desired directory (e.g. desktop), and do `git clone URL` (URL is the link you copied from GitHub)
  4- replace the model_growth.py you made for the one that is in the Assignment directory. (or alternatively fill in a to d in the model_growth.py file that you have just cloned)
  [in your git terminal, cd to the repo directory]
  5- do `git status` and see that now the python file is shown as chnaged and needs to be tracked
  6- do the steps necessary to track your change:
  **a**
  **b**
  7- push to your origin (you can see the name of your local )
  **c**
  8- go to GitHub and view that your repo is now different than the class repo (something like the figure below) and make a pull request
  **d** there will be a mark for seeing your pull request. although we won't merge the pull requests.
![Figure showing the github repo pull request](PR.png)
