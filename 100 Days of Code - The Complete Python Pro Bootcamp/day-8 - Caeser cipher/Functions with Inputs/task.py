def greet():
    print("Hello Angela")
    print("How do you do Jack Bauer?")
    print("Isn't the weather nice?")

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")
greet()

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

greet_with("Jack Bauer", "Nowhere")

greet_with("Nowhere", "Jack Bauer")