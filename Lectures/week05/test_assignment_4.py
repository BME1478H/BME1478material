from glob import glob
import sys, io, os
import numpy as np

# hide traceback, works in Python <= 3.6
# if still printing a lot, try setting to 0 (Python > 3.7)
#sys.tracebacklimit = None

def test_fns(local_vars, errors):
    try:
        fn = local_vars['patient_summary']
        a = np.array([[0,0,0],[0,1,2],[1,2,3]])
        output = fn(a, 'mean')
        expected = np.mean(a,axis=1)
        if not np.equal(output, expected).all():
            error_msg = f"Output was {output} but expected {expected}"
            errors.append(f"Incorrect calculation with function patient_summary(), {error_msg}")
    except KeyError as e:
        errors.append(f"patient_summary undefined, {e}")

    return errors


def test_detect_problems(local_vars, errors):
    try:
        fn = local_vars['detect_problems']
    except KeyError as e:
        errors.append(f"detect_problems undefined, {e}")

    a = np.array([0,1,2],)



def test_Experiment_class(local_vars, errors):
    try:
        Experiment = local_vars["Experiment"]
        exp = Experiment(1)
    except Exception as e:
        errors.append(f"class Experiment not defined, {e}")

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
        tests = [test_Experiment_class, test_fns]
        for fn in tests:
            error_summary = fn(local_vars, error_summary)

    return error_summary


def main():
    assignments_directory = sys.argv[-1].rstrip('/')
    fnames = glob(f'{assignments_directory}/*.py*')
    summary_text = {}

    for file_path in fnames:
        file_name = os.path.basename(file_path)
        print(file_name)
        errors = check_scripts(file_path)

        if len(errors):
            msg = "\n".join(errors)
        else:
            msg = "All checks passed."

        summary_text[file_name] = msg

    with open("assignment_summary.txt", "w") as text_file:
        for student in summary_text:
            print(f"{student}: \n{summary_text[student]}\n", file=text_file)

    print("Completed Successfully")

if __name__ == "__main__":
    main()
