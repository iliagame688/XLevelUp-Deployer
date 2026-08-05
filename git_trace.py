import subprocess
import traceback


old_run = subprocess.run
old_check_output = subprocess.check_output
old_check_call = subprocess.check_call


def trace_cmd(cmd, *args, **kwargs):

    text = str(cmd)

    if "git" in text:

        print("\n===== GIT COMMAND DETECTED =====")
        print(cmd)
        print("===== STACK =====")

        traceback.print_stack()


    return old_run(cmd, *args, **kwargs)



def trace_output(cmd, *args, **kwargs):

    if "git" in str(cmd):

        print("\n===== GIT OUTPUT COMMAND =====")
        print(cmd)
        traceback.print_stack()


    return old_check_output(cmd,*args,**kwargs)



def trace_call(cmd,*args,**kwargs):

    if "git" in str(cmd):

        print("\n===== GIT CALL COMMAND =====")
        print(cmd)
        traceback.print_stack()


    return old_check_call(cmd,*args,**kwargs)



subprocess.run = trace_cmd
subprocess.check_output = trace_output
subprocess.check_call = trace_call


from Core.main import start

start()

