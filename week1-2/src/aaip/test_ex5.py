
import os
import tempfile
 
import ex5

base = tempfile.mkdtemp()
print("Working in temporary folder:", base)
print()
 
# 1. create_project_structure
print("=== 1. create_project_structure(base, 'demo_project') ===")
result = ex5.create_project_structure(base, "demo_project")
print("Return value:", result)
project = os.path.join(base, "demo_project")
print()
 
# 2. traverse_directory
print("=== 2. traverse_directory(project) ===")
result = ex5.traverse_directory(project)
print("Return value:", result)
print()
 
# 3. file_metadata
print("=== 3. file_metadata(README.md) ===")
result = ex5.file_metadata(os.path.join(project, "README.md"))
print("Return value:", result)
print()
 
# 4. find_files_by_extension
print("=== 4. find_files_by_extension(project, '.py') ===")
result = ex5.find_files_by_extension(project, ".py")
print("Return value:", result)
print()
 
print("=== 4b. find_files_by_extension(project, '.md') ===")
result = ex5.find_files_by_extension(project, ".md")
print("Return value:", result)
print()
 
# 5. delete_files_and_directories
print("=== 5. delete_files_and_directories(project) ===")
print("Exists before:", os.path.exists(project))
result = ex5.delete_files_and_directories(project)
print("Return value:", result)
print("Exists after:", os.path.exists(project))
print()
 
# Clean up the temporary base folder
os.rmdir(base)
print("Done.")


