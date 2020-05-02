import ntpath
import os
import subprocess

from commands.Command import Command


class Executor(Command):

    def __init__(self, input_file: str, program_for_execution) -> None:
        self.file_path = input_file
        self.program = program_for_execution

    def execute(self) -> None:
        if self.program == "python" or self.program == "bash":
            subprocess.call([self.program, self.file_path])
        elif self.program == "java":
            subprocess.call(["javac", self.file_path])
            subprocess.call([self.program, self.file_path])
        elif self.program == "kotlin":
            jar_file_name = os.path.splitext(ntpath.basename(self.file_path))[0] + ".jar"
            subprocess.call(["kotlinc", self.file_path, "-include-runtime", "-d", jar_file_name])
            subprocess.call(["java", "-jar", jar_file_name])

        print("{} executed...".format(ntpath.basename(self.file_path)))
