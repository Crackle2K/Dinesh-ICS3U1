"""
Author: Dinesh Sinnathamby
Date: February 9th, 2026
Description: This program takes the number of explorers, the number of dead explorers, and the name of the quest leader as input, and then outputs a story about the quest for diamonds.
"""


explorersAmount = int(input("Enter the number of explorers: "))
deadExplorers = int(input("Enter the number of dead explorers: "))
questLeader = input("Enter the name of the quest leader: ")

print(f"{questLeader} led an army of brave exploring kids on a quest for diamonds.")
print(f"Unforunately, {deadExplorers} of the explorers died during the quest, fighting off monsters.")
print(f"Only {explorersAmount - deadExplorers} explorers survived.")

print("The survivors were about to give up, but found a secret passage that led them to 750 diamonds.") 
print(f"They were able to escape with the diamonds, but {questLeader} kept {750 % (explorersAmount - deadExplorers)} diamonds for himself, and shared the rest with the survivors.")