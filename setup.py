import subprocess

def goback():
    process = subprocess.Popen(["cd","/home/pal/Lampe_Robotique"])
    process.wait()

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
    process = subprocess.Popen(["cd", "/home/pal/inria_wbc/build"]) #cmake -DCMAKE_PREFIX_PATH=~/install ..
    process.wait()
    process = subprocess.Popen(["cmake", "-DCMAKE_PREFIX_PATH=~/install", ".."]) #
    process.wait()
    goback()

# AJOUTER DES OPTIONS ICI
menu_options = {
    1: ['Build & Copie (OBLIGATOIRE)', setupProject],
    2: ['Executer Exemple RobotDart Lampe', executeRbLamp],
    3: ['Inria WBC Build Franka', buildFranka],
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