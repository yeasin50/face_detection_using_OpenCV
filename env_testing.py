def pyVersion():
    import platform
    print('[OK]: python version: '+platform.python_version())

def testCV2():
    try:
        import cv2
        print("[OK]: opemCV package satisfed")
    except:
        print("[WARNING]::please install opencv. use this command => pip install opencv-python")
        print("OR => Official doc: https://pypi.org/project/opencv-python/")
        print('''
            if you still face problem
            simply goto terminal
            - pip uninstall numpy
            after that use old version of numpy
            - pip install numpy==1.19.3
        ''')

def testNumpy():
    try:
        import numpy
        numpyVer = numpy.version.version

        print("[OK]: numpy version: "+ numpyVer, end='   ')
        
        if(numpyVer!="1.19.3"):
            print("it's better using numpy:1.19.3")
    except:
        print("[WARNING]:: please install numpy. use this command => pip install numpy==1.19.3")

def testPillow():
    try:
        from PIL import Image
        print("[OK]: pillow package satisfy")
    except:
        print("[WARNING]:: please install pillow. use this command => pip install Pillow")
        print("=> Official doc: https://pypi.org/project/Pillow/")

def testCVImage():
    try:
        import cv2
        img = cv2.imread("assets/L.jpg")
        cv2.imshow("output",img)
        print("[INFO]: Exit the openned IMage window")
        cv2.waitKey(0)
    except:
        print("failed to load image")

print("\n Environment checkUp....\n")
pyVersion()
testNumpy()
testCV2()
testPillow()
testCVImage()

