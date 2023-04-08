import subprocess

# git clone https://github.com/MOBISARE/Lampe-Robotique.git

# AJOUTER DES FONCTIONS ICI
def setupProject():
    process = subprocess.Popen(["chmod","+x","build_copy.sh"])
    process.wait()
    process = subprocess.Popen(["/home/pal/Lampe-Robotique/build_copy.sh"])
    process.wait()

def executeRbLamp():
    process = subprocess.Popen(["/home/pal/robot_dart/build/lampe"])
    process.wait()

def buildLampe():
    process = subprocess.Popen(["cp", "-r", "/home/pal/Lampe-Robotique/inria_test/lampe", "/home/pal/inria_wbc/etc/lampe"])
    process.wait()
    process = subprocess.Popen(["cp", "/home/pal/Lampe-Robotique/inria_test/lampe.cpp", "/home/pal/inria_wbc/src/robot_dart/lampe.cpp"])
    process.wait()
    process = subprocess.Popen(["mkdir", "/home/pal/install/share/utheque/lampe"])
    process.wait()
    process = subprocess.Popen(["cp", "/home/pal/Lampe-Robotique/lampe.urdf", "/home/pal/install/share/utheque/lampe/lampe.urdf"])
    process.wait()
    process = subprocess.Popen(["cp", "/home/pal/Lampe-Robotique/inria_test/CMakeLists.txt", "/home/pal/inria_wbc/src/robot_dart/CMakeLists.txt"])
    process.wait()
    process = subprocess.Popen(["cmake", "-DCMAKE_PREFIX_PATH=~/install", "-S", "/home/pal/inria_wbc", "-B", "/home/pal/inria_wbc/build"])
    process.wait()
    process = subprocess.Popen(["make", "/home/pal/inria_wbc/build/lampe"])
    process.wait()
    process = subprocess.Popen(["make", "/home/pal/inria_wbc/build/lampe_graphics"])
    process.wait()

# AJOUTER DES OPTIONS ICI
menu_options = {
    1: ['Build & Copie (OBLIGATOIRE)', setupProject],
    2: ['Executer Exemple RobotDart Lampe', executeRbLamp],
    3: ['Inria WBC Copie & Build Lampe', buildLampe],
}

# PAS BESOIN DE TOUCHER
keys = menu_options.keys()
def print_menu():
    print("=>")
    for key in keys:
        print (key, '--', menu_options[key][0])

try:
    while(True):
        print_menu()
        option = int(input('Veuillez choisir une option ([0-9] + ENTER) : '))
        if option in keys:
            menu_options[option][1]()

except KeyboardInterrupt:
    print("\nBye")