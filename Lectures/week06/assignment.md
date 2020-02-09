# Assignment

## Part 1 (3.5 marks)
Turn the code for predicting population growth in bacteria into a command line script:

Our collaborator sends us a csv file named `bacteria.csv`, they have started with a colony of 300 bacteria and have counted the population 100 times in the course of 10 days. We hypothesize that the daily growth has an exponential model and we want to find the rate that bests fit an exponential model to the data. We want a script that takes the csv file, and the range of rates that we desire and returns the rate with the best fit. Something like below in the command line:

```bash
python model_growth.py bacteria.csv 0.1 1 0.1
```

where 1st argument (after script name) is the file containing our data (bacteria.csv), and the next 3 arguments (0.1, 1, and 0.1) indicate the start, stop, and step sized needed, respectively, to create our range of rates. 

Create a python script called `model_growth.py` that uses the following example solution code to Assignment 3 and turn it into a command line script.
The places you need to fill in code are indicated via `**(a-e, marks allocated)**`:

```Python
# import libraries used in this script
**(a, 1 mark)  ....**

def main():
    # read in the data from the .csv passed to our script
    filename = **(b, 0.5 marks)...**
    experiment_data = **(d, 0.5 marks)...**

    # store the command-line arguments that represent the start, stop, and step size in the variable rate_params
    rate_params = **(c, 0.5 marks)....**
    # note: since the parameters that are read by sys.argv are strings, we have to convert them to floats using float(a_string)
    range_rate = np.arange(float(rate_params[0]), float(rate_params[1]), float(rate_params[2]))

    # define a function that calculates mean squared error
    def squared_error(prediction, data):
        residual = prediction - data
        mse = (residual**2).mean()          
        return mse

    # try the parameters and choose the one with the smallest squared error
    mse = []
    # note two modifications below: we are taking the N0 and the time vector from data
    N0 = experiment_data[0]
    t = np.linspace(0, 10, len(experiment_data))
    for r in range_rate:
        prediction = N0*np.exp(r*t)
        mse.append(squared_error(prediction, experiment_data))

    best_fit = range_rate[np.argmin(mse)]
    print('We predict the rate of growth of this bacterial population to be', best_fit)
    
    
# write the code necessary to make sure the main() function is called when we run the script from command line
**(e, 1 mark)...**

```
save and close.
Try for yourself to run the script in the command line with a few parameter ranges for the dataset shared with you. for example:
```
python model_growth.py bacteria.csv 0 2 0.1
```
We will share the best fit rate later and you can check if you got close to the right answer (no marks is dedicated to this part).

## Part 2 (2.5 marks)
Fork the class repository, change the script `model_growth.py` as you did in the first section of this assignment, and open a pull request to the [class repo](https://github.com/BME1478H/Winter2020class). Step by Step instructions for this are provided below. **a**, **b**, **c**, **d** stand for commands or actions that have marks.

If you already have forked the class repo you can jump to step 4.

  1. fork on GitHub
  2. copy the link for cloning
  3. open a terminal in your desired directory (e.g. desktop), and run `git clone <URL>` (replace <URL> with the link you copied from your fork on Github)
  4. change to the cloned directory in terminal.
  5. substitute the `model_growth.py` you made for the one in the Assignment directory (you can either replace the file or copy over the content).

  Note: that it is often preferred to create a separate branch for new features rather than making changes directly to your master branch, but we're skipping that step in this assignment.

  6. run `git status` and confirm that `model_growth.py` shows up as a modified file (if you changed the filename it might show up as an untracked file instead).
  7. do the steps necessary to track your change (i.e. add the changed file to the staging area, and commit with an explanatory commit message). List the two commands you needed to run:

     **(a, 0.5 marks)**

     **(b, 0.5 marks)**

  8. push your updated local repo to the remote named "origin" (which is the nickname for your fork). Write the command you needed to run:

     **(c, 0.5 marks)**

  9. go to your fork on GitHub, confirm that your repo is now ahead of the class repo (something like the figure below), and open a pull request.

     **(d, 1 mark)**

  There will be a mark for seeing your pull request. although we won't merge the pull requests. Here's what it looks like:

![Figure showing the status before pull request](https://github.com/BME1478H/Winter2020class/blob/master/Assignment/PR.PNG)

## Deliverables:
- Part 1: Fill in `model_growth.py` and make a copy (somewhere else, not in your git repository folder) renamed as `first_last_assignment5.py` (replacing first and last with your name).
- Part 2: Write the git commands needed to complete **a-c** at the bottom of your `first_last_assignment5.py`, e.g. 
```
# all lines should start with #
# question a
# commands go here
# question b
# commands go here
# question c
# commands goes here

```
TAs will check the class repo for receiving your pull request (for **d**).

**Submit `first_last_assignment5.py` to Quercus Assignment #5**
