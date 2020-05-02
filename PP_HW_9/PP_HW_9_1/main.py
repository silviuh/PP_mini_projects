from responsability_chain.BashHandler import BashHandler
from responsability_chain.GenericHandler import GenericHandler
from responsability_chain.JavaHandler import JavaHandler
from responsability_chain.KotlinHandler import KotlinHandler
from responsability_chain.PythonHandler import PythonHandler

if __name__ == '__main__':
    bash_handler = BashHandler()
    java_handler = JavaHandler()
    python_handler = PythonHandler()
    kotlin_handler = KotlinHandler()
    generic_handler = GenericHandler()

    bash_handler. \
        set_next(python_handler). \
        set_next(java_handler). \
        set_next(kotlin_handler). \
        set_next(generic_handler)

print(bash_handler.handle("iti poti alege O CALE din directory-ul test_files sau ce vale vrei tu"))
