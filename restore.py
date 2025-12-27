from pathlib import Path
import subprocess
import random
import string


def getUser(): return subprocess.check_output(
    "whoami").decode().strip().split("\\")[-1]


USER = getUser()
FC_26_PATH = Path(f"C:\\Users\\{USER}\\AppData\\Local\\EA SPORTS FC 26")
NVIDIA_PATH = Path(f"C:\\Users\\{USER}\\AppData\\Local\\NVIDIA")


class RestoreFilesFC26:
    def __init__(self):

        if not self.__check_os():
            raise EnvironmentError(
                "This script can only be used on Windows systems.")
        self.__check_fc26_nvidia_dir()
        pass

    def start_configuration(self) -> None:
        print("Starting FC26 files restoration...")
        self.__configure_fc26_files()
        print("FC26 files restoration completed.")
        print("Starting NVIDIA files restoration...")
        self.__configure_nvidia_files()
        print("NVIDIA files restoration completed.")
        print("All operations completed successfully.")
        print("You can now restart your computer for the changes to take effect.")
        pass

    def __configure_fc26_files(self) -> None:
        # rd windows command to delete folder and its contents
        subprocess.run(["rd", "/s", "/q", str(FC_26_PATH) + "\\fcsetup"],
                       shell=True, check=False)
        subprocess.run(["rd", "/s", "/q", str(FC_26_PATH) + "\\umcache"],
                       shell=True, check=False)
        subprocess.run(["rd", "/s", "/q", str(FC_26_PATH) + "\\filesystemcache"],
                       shell=True, check=False)
        subprocess.run(["rd", "/s", "/q", str(FC_26_PATH) + "\\twinkle"],
                       shell=True, check=False)
        subprocess.run(["rd", "/s", "/q", str(FC_26_PATH) + "\\twinkle_temp"],
                       shell=True, check=False)

        # rename file
        fcsetup_file = str(FC_26_PATH) + "\\fcsetup.ini"
        fcsetup_file_renamed = str(FC_26_PATH) + "\\fcsetup_" + self.__get_random_string() + \
            ".ini"
        Path(fcsetup_file).rename(fcsetup_file_renamed)
        pass

    def __configure_nvidia_files(self) -> None:
        # DELETE ALL THE CONTENT INSIDE OF NVIDIA PATH
        DX_CACHE_PATH = str(NVIDIA_PATH) + "\\DXCache"
        GL_CACHE_PATH = str(NVIDIA_PATH) + "\\GLCache"
        for path in [DX_CACHE_PATH, GL_CACHE_PATH]:
            if Path(path).exists() and Path(path).is_dir():
                subprocess.run(["del", "/q", str(path) + "\\*.*"],
                               shell=True, check=False)
                subprocess.run(["for", "/d", "%i", "in", f"({path}\\*)", "do",
                                "rmdir", "/s", "/q", "%i"],
                               shell=True, check=False)

    def __check_fc26_nvidia_dir(self) -> bool:

        if not FC_26_PATH.exists() or not FC_26_PATH.is_dir():
            raise FileNotFoundError(
                "The FC26 directory does not exist, if you have move it, please update the path at the code.")
        if not NVIDIA_PATH.exists() or not NVIDIA_PATH.is_dir():
            raise FileNotFoundError(
                "The NVIDIA directory does not exist, if you have move it, please update the path at the code.")
        return True

    def __check_os(self) -> bool:
        import platform
        return platform.system() == "Windows"

    def __get_random_string(self, length: int = 8) -> str:
        letters = string.ascii_lowercase + string.digits + string.ascii_uppercase
        return ''.join(random.choice(letters) for i in range(length))


if __name__ == "__main__":
    my_class = RestoreFilesFC26()
    my_class.start_configuration()
