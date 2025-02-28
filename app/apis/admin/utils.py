import subprocess

def get_disk_usage(parameters: str):
    
    allowed_parameters = [
        "-a",
        "-B",
        "-h",
        "-H",
        "-i",
        "-k",
        "-l",        
    ]

    param_list = parameters.split()
    
    for param in param_list:
        if param not in allowed_parameters:
            raise ValueError(f"Parameter '{param}' is not allowed.")

    command = ["df", "-h"] + param_list
    
    try:
        result = subprocess.run(
            command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )
        if result.returncode != 0:
            raise Exception(f"Command failed: {result.stderr}")
        usage = result.stdout.strip()
    except Exception as e:
        raise Exception(f"An unexpected error occurred: {str(e)}")
    
    return usage
