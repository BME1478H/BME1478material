from glob import glob
import sys, io, os
import numpy as np

# hide traceback, works in Python <= 3.6
# if still printing a lot, try setting to 0 (Python > 3.7)
#sys.tracebacklimit = None

def test_squared_error(local_vars, errors):
    try:
        fn = local_vars['squared_error']
    except KeyError as e:
        errors.append(f"squared_error undefined, {e}")

    a = np.array([1,2,3])
    b = np.array([4.2,1,6.3])
    output = fn(a, b)
    expected = ((a-b)**2).mean()
    if output != expected:
        error_msg = f"Output was {output} but expected {expected}"
        errors.append(f"Incorrect calculation with function squared_error(), {error_msg}")
    return errors

def test_variables(vars_dict, errors):
    variables_exact =  {'rate':0.4,
                 'N0': 100}

    variables_fuzzy = ['t', 'best_fit', 'population_size',
                       'population_size_noise', 'range_rate']

    t = np.arange(0,10,.2)
    range_rate = np.arange(.1,1.1,.1)
    # check existence and values of variables
    for i in variables_exact:
        if ((i in vars_dict) or (i.lower() in vars_dict)):
            if vars_dict[i] != variables_exact[i]:
                errors.append(f"Variable {i} defined as {vars_dict[i]} when it should be {variables_exact[i]}")
        else:
            errors.append(f"Variable {i} is undefined")

    # checking variables with more flexible definitions
    for i in variables_fuzzy:
        if not ((i in vars_dict) or (i.lower() in vars_dict)):
            errors.append(f"Variable {i} is undefined")

    # t is the correct range of values
    try:
        if not np.equal(vars_dict['t'][:10],t[:10]).all():
            errors.append(f"Variable t defined as {vars_dict['t'][:10]} when it should be {t[:10]} \
                \n (First 10 indices)")
    except Exception as e:
        errors.append(f"variable t undefined, {e}")

    # range_rate is the correct range of values
    try:
        if not np.equal(vars_dict['range_rate'][:5],range_rate[:5]).all():
            errors.append(f"Variable range_rate defined as {vars_dict['range_rate'][:5]} when it should be {range_rate[:5]}")
    except Exception as e:
        errors.append(f"Range_rate undefined, e")


    # best_fit is approximately 0.4
    try:
        if not np.isclose(vars_dict['best_fit'],0.4, atol=0.001):
            errors.append("Variable best_fit is {vars_dict['best_fit']} but should be 0.4")
    except Exception as e:
        errors.append(f"Undefined variable, {e}")

    # population_size should be same size as t
    try:
        if len(vars_dict['population_size']) != len(vars_dict['t']):
            errors.append("population_size ({len(vars_dict[population_size])}) should be same length as t ({len(vars_dict[t])})")
    except Exception as e:
        errors.append(f"Undefined variable, {e}")

    # mse should be same size as range_rate
    try:
        if len(vars_dict['mse']) != len(vars_dict['range_rate']):
            errors.append(f"mse ({len(vars_dict['mse'])}) \
                should be same length as range_rate ({len(vars_dict['range_rate'])})")
    except Exception as e:
        errors.append(f"Undefined variable, {e}")

    return errors


def check_scripts(fname):
    error_summary = []
    with open(fname) as f:
        try:
            #suppress prints from student script
            suppress_prints = io.StringIO()
            sys.stdout = suppress_prints
            exec(f.read())
            # now restore stdout function
            sys.stdout = sys.__stdout__
        except Exception as e:
            error_summary.append(f"Error when executing script., {e}")
            # stop here as the rest can't be checked
            return error_summary
        local_vars = locals()
        test_fns = [test_squared_error, test_variables]
        for fn in test_fns:
            error_summary = fn(local_vars, error_summary)

    return error_summary


def main():
    assignments_directory = sys.argv[-1].rstrip('/')
    fnames = glob(f'{assignments_directory}/*.py*')
    summary_text = {}

    for file_path in fnames:
        file_name = os.path.basename(file_path)
        print(file_name)
        errors = check_script(file_path)

        if len(errors):
            msg = "\n".join(errors)
        else:
            msg = "All check passed."

        summary_text[file_name] = msg

    with open("assignment_summary.txt", "w") as text_file:
        for student in summary_text:
            print(f"{student}: \n{summary_text[student]}\n", file=text_file)

    print("Completed Successfully")

if __name__ == "__main__":
    main()