import subprocess
import sys

def create_django_project(project_name):
    try:
        import django
    except ImportError:
        subprocess.check_call([sys.executable,"-m","pip","install","Django"])
        import django
    subprocess.check_call(["django-admin","startproject",project_name])

if __name__=="__main__":
    if len(sys.argv)<2:
        print("Provide a project name.")
    else:
        project_name=sys.argv[1]
        create_django_project(project_name)
        