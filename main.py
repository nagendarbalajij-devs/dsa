import sys
import shutil
import os
def run_problem(problem):
    print(problem)


if __name__ == "__main__":
    try:
        if sys.argv[1].lower() == "add":
            p = int(sys.argv[2])
            
            c_src = os.path.join("src", "template.py")
            t_src = os.path.join("assets", "template.md")

            c_dst = os.path.join("src", f"problem_{p}.py")
            t_dst = os.path.join("assets", f"{p}.md")
            
            shutil.copy(c_src,c_dst)
            shutil.copy(t_src,t_dst)
        else:
            c_src = os.path.join("src", f"problem_{sys.argv[1]}.py")
            if os.path.exists(c_src):
                os.system(f"python -c \"from src.problem_{sys.argv[1]} import main; main()\"")
            else:
                raise FileNotFoundError
    except IndexError:
        print("Check args!")
    except ValueError:
        print("Enter a leetcode problem number!")
    except FileNotFoundError:
        print("Problem not found") 