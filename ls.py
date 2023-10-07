import subprocess

def run_ls():
    result = subprocess.run(['ls', '-l'], capture_output=True, text=True)
    print(result.stdout)

if __name__ == "__main__":
    run_ls()
