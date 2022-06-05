from os.path import basename, isfile, join
import glob

def update(path:str) -> None:
    modules = glob.glob(join(path, "*.py"))
    modulesList = [basename(module)[:-3] for module in modules if isfile(module) and not module.endswith("__init__.py")]

    # print(modulesList)

    with open(f"{path}/__init__.py", "w") as file:
        file.write(f"__all__ = {modulesList}")

# update("src/keyboardTemplates")
