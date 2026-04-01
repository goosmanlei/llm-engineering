import modal
import sys
import platform

app = modal.App("example-get-started")

@app.function()
def check_python():
    print("=== Python Info ===")
    print("Executable:", sys.executable)
    print("Version:", sys.version)
    print("Platform:", platform.platform())

@app.function(gpu="A10G")  # 可选，加上更明显
def inspect_machine():
    import os
    import sys
    import platform
    import subprocess

    print("=== 🧠 Python ===")
    print("Executable:", sys.executable)
    print("Version:", sys.version)

    print("\n=== 🖥️ OS ===")
    print("Platform:", platform.platform())

    print("\n=== CPU ===")
    print(subprocess.getoutput("lscpu"))

    print("\n=== Memory ===")
    print(subprocess.getoutput("free -h"))

    print("\n=== Disk ===")
    print(subprocess.getoutput("df -h"))

    print("\n=== GPU ===")
    print(subprocess.getoutput("nvidia-smi"))

    print("\n=== ENV (部分) ===")
    for k, v in os.environ.items():
        if any(x in k.lower() for x in ["cloud", "aws", "gcp", "modal"]):
            print(f"{k}={v}")

@app.local_entrypoint()
def main():
	check_python.remote()
	inspect_machine.remote()
