def dhm():
    alice_secret = int(input("\nEnter Alice's Secret Number: "))
    bob_secret = int(input("Enter Bob's Secret Number: "))
    # Confirmed good numbers:
    # 982734869235
    # 339829374235
    # 882377523950
    # 234987235987
    # 3987235455
    # 4625746726
    # 2354754234
    # 4747566324
    # 397249857239
    # 245257435634
    # 89151432
    # 74753929
    # 617961596
    # 458364697
    # 1065832294
    # 83257424847
    # 994673453480
    # 883666651

    g = 3
    p = 6840273601699

    print(f'generator: {g}')
    print(f'prime: {p}')


    alice_public = (g ^ alice_secret) % p
    bob_public = (g ^ bob_secret) % p

    print(f"Alice's Public: {alice_public}")
    print(f"Bob's Public: {bob_public}")

    alice_bob_private = (bob_public ^ alice_secret) % p
    bob_alice_private = (alice_public ^ bob_secret) % p

    print(f"Alice's Private Calculation: {alice_bob_private}")
    print(f"Bob's Private Calculation: {bob_alice_private}")

if __name__ == "__main__":
    while True:
        dhm()