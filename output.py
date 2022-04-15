import  os
from utils import output_exists
from file_ops import clean_up
def fetch_output(exec_id):
    '''
    This function fetches the output of the code
    '''
    if output_exists(exec_id):
        with open(os.path.join('outputs',exec_id+'.txt'),'r') as f:
            output = f.read()
        status = "success"
    else:
        status = "No output found"
        output = " "
    clean_up(os.path.join('outputs',exec_id+'.txt'))
    return {"status": status, "output": output}