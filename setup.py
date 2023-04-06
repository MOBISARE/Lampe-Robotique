import subprocess

# AJOUTER DES FONCTIONS ICI
def setupProject():
    process = subprocess.Popen(["chmod","+x","build_copy.sh"])
    process.wait()
    process = subprocess.Popen(["./build_copy.sh"])
    process.wait()

def executeRbLamp():
    process = subprocess.Popen(["/home/pal/robot_dart/build/lampe"])
    process.wait()

def buildFranka():
    process = subprocess.Popen(["cmake", "-DCMAKE_PREFIX_PATH=~/install", "-S", "/home/pal/inria_wbc", "-B", "/home/pal/inria_wbc/build"])
    process.wait()
    process = subprocess.Popen(["make", "/home/pal/inria_wbc/build/franka_graphics"])
    process.wait()

def executeFranka():
    process = subprocess.Popen(["/home/pal/inria_wbc/build/franka_graphics"])
    process.wait()

# AJOUTER DES OPTIONS ICI
menu_options = {
    1: ['Build & Copie (OBLIGATOIRE)', setupProject],
    2: ['Executer Exemple RobotDart Lampe', executeRbLamp],
    3: ['Inria WBC Build Franka', buildFranka],
    4: ['Inria WBC Execute Franka (GRAPHICS)', executeFranka],
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