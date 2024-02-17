def compare(alice,bob):
    
    alice_score = 0
    bob_score = 0
    
    # index 0
    if alice[0] > bob[0]:
        alice_score = alice_score + 1
    if bob[0] > alice[0]:
        bob_score = bob_score + 1

    # index 1
    if alice[1] > bob[1]:
        alice_score = alice_score + 1
    if bob[1] > alice[1]:
        bob_score = bob_score + 1

    # index 2
    if alice[2] > bob[2]:
        alice_score = alice_score + 1
    if bob[2] > alice[2]:
        bob_score = bob_score + 1

    score = [alice_score, bob_score]

    return score
        
alice = list(map(int, input().split()))
bob = list(map(int, input().split()))

x = compare(alice, bob)
print(x[0], x[1])
