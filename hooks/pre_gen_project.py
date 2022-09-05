import re
import sys


MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

package_name = '{{cookiecutter.package_name}}'
project_name = '{{cookiecutter.project_name}}'

def package_name_validation():
    if not re.match(MODULE_REGEX, package_name):
        print(f"ERROR: {package_name} is not a valid Python package name. Alphanumeric characters or underscores only")
        #Exit to cancel project
        sys.exit(1)
        
def project_name_validation():
    if not re.match(MODULE_REGEX, project_name):
        print(f"ERROR: {project_name} is not a valid Python project name. Alphanumeric characters or underscores only")
        #Exit to cancel project
        sys.exit(1)
        
if __name__ == "__main__":
    package_name_validation()
    project_name_validation()