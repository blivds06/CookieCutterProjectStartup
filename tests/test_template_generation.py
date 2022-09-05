
import os

import pytest
from cookiecutter.exceptions import FailedHookException

@pytest.fixture
def default_context():
    return {
        "project_name": "My_Test_Project",
        "package_name": "mytestproject",
        }

class EmptyDirectoryError(Exception):
    """Raised when a directory is empty"""
    
def check_no_empty_directories(root_dir):
    for root, folders, files in os.walk(root_dir):
        if not (folders or files):
            raise EmptyDirectoryError(f"The folder {root} is empty.")
            
def test_project_generation(cookies, default_context):
    """Test a valid template is rendered"""
    result = cookies.bake(extra_context={**default_context})
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name == default_context["project_name"]
    assert result.project_path.is_dir()
    check_no_empty_directories(result.project_path)
    
def test_invalid_package_name(cookies,default_context):
    """A package_name with spaces should fail the pre-generation hook"""
    default_context.update({"package_name": "name with spaces"})
    result = cookies.bake(extra_context=default_context)
    assert result.exit_code != 0
    assert isinstance(result.exception, FailedHookException)
    
def test_invalid_project_name(cookies,default_context):
    """A package_name with spaces should fail the pre-generation hook"""
    default_context.update({"project_name": "name with spaces"})
    result = cookies.bake(extra_context=default_context)
    assert result.exit_code != 0
    assert isinstance(result.exception, FailedHookException)