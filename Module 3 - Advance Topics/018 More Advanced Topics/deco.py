# Decorator display

def enhance_func(func):
    def wrapper(argu):
        feature = input("What feature you want to add? ")
        print(f"{argu} enhanced with feature {feature}")
        func(argu)
    return wrapper

@enhance_func
def robot(name):
    print(f"Robot '{name}' is activated")

robot("Alexa")

