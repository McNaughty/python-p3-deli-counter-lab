def line(katz_deli):
    if katz_deli:
        queue_details = [f"{index + 1}. {person}" for index, person in enumerate(katz_deli)]
        print("The line is currently:", " ".join(queue_details))
    else:
        print("The line is currently empty.")


def take_a_number(katz_deli, name):
    last_number = len(katz_deli) + 1
    print(f"Welcome, {name}. You are number {last_number} in line.")
    katz_deli.append(name)
    # print(katz_deli)

# katz_deli = ["Logan", "Avi", "Spencer"]
# name = "Winnie"
# print(take_a_number(katz_deli, name))
    

def now_serving(katz_deli):
    if katz_deli:
        next_customer = katz_deli[0]
        print(f"Currently serving {next_customer}.")
        del katz_deli[0]
    else:
        print(f"There is nobody waiting to be served!")