import sys
import re
import spacy
from datetime import datetime
import pkg_resources

# Get the library versions
spacy_version = pkg_resources.get_distribution("spacy").version
python_version = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"

# Create and write the requirements.txt file
with open("requirements.txt", "w") as f:
    f.write(f"spacy=={spacy_version}\n")
    f.write(f"python=={python_version}\n")
