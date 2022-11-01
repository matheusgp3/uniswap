import os
from dotenv import load_dotenv
import pathlib

os.getcwd()
pathlib.Path().resolve()
load_dotenv()
print(os.getenv('secretPhrase'))