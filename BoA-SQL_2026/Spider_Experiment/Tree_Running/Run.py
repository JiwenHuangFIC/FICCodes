from Task_Tree_Running import *
import sys

def main(given_task = "I want to see highest spot gold price of China."):
    if given_task:
        print("Your question is:")
        print(given_task)
        signal, final_code = Task_Tree_Running(root_task = given_task)
        print("########################################################################")
        print("*** The sql code generation process:", signal)
        print("*** The final_code is as follows:")
        print(final_code)
    else:
        print("The default question is this:")
        print("I want to see highest spot gold price of China.")
        signal, final_code = Task_Tree_Running(given_task)
    
if __name__ == "__main__":
    if len(sys.argv) > 1:
        root_task = sys.argv[1]
        main(root_task)
    else:
        print("您没有输入任何参数，我们将根据默认的问题启动sql代码生成程序。")
        print("We would start the code generation process with default question.")
        main()