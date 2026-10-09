#%% md
# Թեմա 20 — Լուծումներ

#%% code
import importlib.metadata as metadata
from pathlib import Path

# Required 1 and 2 - what is installed, and where it lives
import numpy
import pandas
import matplotlib

for module in [numpy, pandas, matplotlib]:
    name = module.__name__
    print(f"{name:<12} {metadata.version(name):<10} {Path(module.__file__).parent}")

#%% code
# Required 3 - the file a colleague needs
requirements = "\n".join(
    f"{name}=={metadata.version(name)}"
    for name in ["numpy", "pandas", "matplotlib"]
) + "\n"

Path("requirements.txt").write_text(requirements, encoding="utf-8")
print(requirements)

#%% code
# Required 4 - four imports, one function
import numpy
print(numpy.mean([1, 2, 3]))

import numpy as np
print(np.mean([1, 2, 3]))

from numpy import mean
print(mean([1, 2, 3]))

from numpy import mean as average
print(average([1, 2, 3]))

#%% code
# Extra 5 - standard library, or installed?
import sys

names = ["json", "numpy", "math", "pandas", "csv", "matplotlib", "datetime"]
for name in names:
    kind = "standard" if name in sys.stdlib_module_names else "installed"
    print(f"{name:<12} {kind}")
