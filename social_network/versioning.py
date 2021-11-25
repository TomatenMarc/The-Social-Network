import sys
import toml

if len(sys.argv) != 2:
    print("Usage: python versioning.py <version>")
    sys.exit(1)
    
version = sys.argv[1]

with open("pyproject.toml", "r") as f:
    toml_file = toml.load(f)
    
toml_file["tool"]["poetry"]["version"] = version

with open('pyproject.toml', 'w') as f:
    new_toml_string = toml.dump(toml_file, f)