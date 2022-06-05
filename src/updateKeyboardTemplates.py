from os.path import basename, isfile, join
import glob


modules = glob.glob(join("src/keyboardTemplates", "*.py"))
modulesList = [basename(module)[:-3] for module in modules if isfile(module) and not module.endswith("__init__.py")]

# print(modulesList)

with open("src/keyboardTemplates/__init__.py", "w") as file:
    file.write(f"__all__ = {modulesList}")
