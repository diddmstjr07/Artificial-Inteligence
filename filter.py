import subprocess


def console(results):
    result = subprocess.run(results, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    stdout_text = result.stdout

    result_string = stdout_text

    lines = result_string.split('\n')

    for index, line in enumerate(lines):
        if index % 2 == 0:
            slicing_result = line[21:22]
            if slicing_result == '(':
                print('No_Objects')
            else:
                last_result = (line[21:22])
                print(last_result)

                return last_result

