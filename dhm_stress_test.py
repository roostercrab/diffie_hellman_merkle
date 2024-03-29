import random
import json


def dhm_stress():
    alice_secret = random.randint(3, 999999999999)
    bob_secret = random.randint(3, 999999999999)

    g = 3
    # p = 28564294577827
    p = 23

    alice_public = (g ^ alice_secret) % p
    bob_public = (g ^ bob_secret) % p

    alice_bob_private = (bob_public ^ alice_secret) % p
    bob_alice_private = (alice_public ^ bob_secret) % p

    if alice_bob_private == bob_alice_private:
        with open("good_numbers.txt", "a+") as file:
            file.write("g= " + json.dumps(g) + '\n')
            file.write("p= " + json.dumps(p) + '\n')
            file.write("a= " + json.dumps(alice_secret) + '\n')
            file.write("b= " + json.dumps(bob_secret) + '\n')
            file.write("ab= " + json.dumps(alice_bob_private) + '\n')
            file.write("ba= " + json.dumps(bob_alice_private) + '\n')
            file.write('\n')
    else:
        with open("bad_numbers.txt", "a+") as file:
            file.write("g= " + json.dumps(g) + '\n')
            file.write("p= " + json.dumps(p) + '\n')
            file.write("a= " + json.dumps(alice_secret) + '\n')
            file.write("b= " + json.dumps(bob_secret) + '\n')
            file.write("ab= " + json.dumps(alice_bob_private) + '\n')
            file.write("ba= " + json.dumps(bob_alice_private) + '\n')
            file.write('\n')


if __name__ == "__main__":
    while True:
        dhm_stress()