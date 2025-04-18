from random import choice

import RedBlackTree



rbt = RedBlackTree.RBT("Dictionary.txt")

print("🔴 Welcome to the Red-Black Tree Dictionary 🔴\n")
wants_to_continue = "yes"

while wants_to_continue.strip().lower() == "yes":
        print("\nAvailable operations:")
        print("• Search for a word         →  (search)")
        print("• Insert a word             →  (insert)")
        print("• Number of words           →  (total)")
        print("• Tree height               →  (height)")
        print("• Black height of the root  →  (black)")

        choice = input("\n👉 Enter your choice: ").strip().lower()

        if choice == "search":
            word = input("🔍 Enter the word: ").strip()
            if rbt.search(word):
                print(f"✅ The word \"{word}\" exists.")
            else:
                print(f"❌ The word \"{word}\" does not exist.")

        elif choice == "insert":
            word = input("➕ Enter the word: ").strip()
            if not rbt.insert(word):
                print(f"⚠️  \"{word}\" is already in the dictionary.")
            else:
                print(f"✅ \"{word}\" inserted successfully.")
                rbt.printTreeDetails()

        elif choice == "total":
            print(f"📚 Total words: {rbt.numberOfNodes(rbt.root)}")

        elif choice == "height":
            print(f"🌲 Tree height: {rbt.height(rbt.root)}")

        elif choice == "black":
            print(f"⚫ Black height of root: {rbt.blackNodes(rbt.root)}")

        else:
            print("❓ Invalid input. Please try again.")

        wants_to_continue = input("\n🔁 Continue? (yes/no): ")

print("\n👋 Thank you for using the Red-Black Tree Dictionary!")



