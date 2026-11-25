import random

def main():
    print("Neuroscience console")
    console_on = True
    while console_on:
        command = input("Neuro_console: ")
        if command == "leave":
            print("Bye!")
            console_on = False
        elif command == "parts":
            print("Neuron estructure:")
            print("-Dendrites: receive information.")
            print("-Soma: body where everything is proccesed.")
            print("-Axon: sends the electrical signal.")
        elif command == "shoot":
            voltage = random.randint(-70,-40)
            print(f"Neuron voltage: {voltage}")
            if voltage >= -55:
                print("Triggered action potential! The signal travels through axon.")
            else:
                print("Weak stimulus. Neuron still repose. Try again")
        else:
            print(f"Command {command} not recognized. Try: parts, shoot or leave.")
            print(f"You have executed the command: {command}")

if __name__ == "__main__":
    main()
