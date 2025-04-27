from arraySequence import ArraySequence, ImmutableArraySequence
from listSequence import ListSequence, ImmutableListSequence
from error import IndexOutOfBoundsError, InvalidInputError

class Menu:
    def __init__(self):
        self.sequences = []  
    def run(self):
        while True:
            print("\nMain Menu:")
            print("1. Create new sequence")
            print("2. Select sequence")
            print("3. Show all sequences")
            print("4. Exit")
            try:
                choice = input("Enter your choice: ")
                if choice == '':
                    raise InvalidInputError()
                choice = int(choice)
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            except InvalidInputError:
                print("Invalid input.")
                continue

            if choice == 1:
                self.createSequence()
            elif choice == 2:
                self.selectSequence()
            elif choice == 3:
                self.showSequences()
            elif choice == 4:
                print("Exiting program. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def createSequence(self):
        print("\nCreate New Sequence:")
        print("1. ArraySequence (mutable)")
        print("2. ImmutableArraySequence")
        print("3. ListSequence (mutable)")
        print("4. ImmutableListSequence")
        try:
            choice = int(input("Choose sequence type (1-4): "))
        except ValueError:
            print("Invalid input. Returning to main menu.")
            return

        if choice < 1 or choice > 4:
            print("Invalid choice. Returning to main menu.")
            return

        elements_input = input("Enter elements separated by space (or leave empty): ")
        elements = []
        if elements_input.strip() != "":
            try:
                elements = [int(x) for x in elements_input.split()]
            except ValueError:
                print("Invalid input for elements. Returning to main menu.")
                return

        seq = None
        if choice == 1:
            seq = ArraySequence(elements)
        elif choice == 2:
            seq = ImmutableArraySequence(elements)
        elif choice == 3:
            seq = ListSequence(elements)
        elif choice == 4:
            seq = ImmutableListSequence(elements)

        self.sequences.append(seq)
        print(f"Sequence created at index {len(self.sequences)-1}.")

    def showSequences(self):
        print("\nExisting Sequences:")
        if not self.sequences:
            print("No sequences available.")
            return
        for idx, seq in enumerate(self.sequences):
            print(f"[{idx}] {seq}")

    def selectSequence(self):
        if not self.sequences:
            print("No sequences available to select.")
            return
        try:
            idx = int(input("Enter sequence index: "))
        except ValueError:
            print("Invalid input. Returning to main menu.")
            return
        if idx < 0 or idx >= len(self.sequences):
            print("Index out of bounds. Returning to main menu.")
            return

        seq = self.sequences[idx]
        while True:
            print(f"\nSelected sequence [{idx}]: {seq}")
            print("Sequence Menu:")
            print("1. Append item")
            print("2. Prepend item")
            print("3. Insert item at index")
            print("4. Remove item at index")
            print("5. Get item at index")
            print("6. Get first item")
            print("7. Get last item")
            print("8. Get subsequence")
            print("9. Print sequence")
            print("0. Back to main menu")
            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if choice == 0:
                break
            elif choice == 1:  # Append
                try:
                    val = int(input("Enter value to append: "))
                except ValueError:
                    print("Invalid input for value.")
                    continue
                if isinstance(seq, (ImmutableArraySequence, ImmutableListSequence)):
                    new_seq = seq.append(val)
                    self.sequences[idx] = new_seq
                    seq = new_seq
                    print(f"Appended. New sequence: {seq}")
                else:
                    seq.append(val)
                    print(f"Appended. Sequence is now: {seq}")

            elif choice == 2:  # Prepend
                try:
                    val = int(input("Enter value to prepend: "))
                except ValueError:
                    print("Invalid input for value.")
                    continue
                if isinstance(seq, (ImmutableArraySequence, ImmutableListSequence)):
                    new_seq = seq.prepend(val)
                    self.sequences[idx] = new_seq
                    seq = new_seq
                    print(f"Prepended. New sequence: {seq}")
                else:
                    seq.prepend(val)
                    print(f"Prepended. Sequence is now: {seq}")

            elif choice == 3:  # Insert
                try:
                    pos = int(input("Enter index to insert at: "))
                    val = int(input("Enter value to insert: "))
                except ValueError:
                    print("Invalid input for index or value.")
                    continue
                try:
                    if isinstance(seq, (ImmutableArraySequence, ImmutableListSequence)):
                        new_seq = seq.insertAt(val, pos)
                        self.sequences[idx] = new_seq
                        seq = new_seq
                        print(f"Inserted. New sequence: {seq}")
                    else:
                        seq.insertAt(val, pos)
                        print(f"Inserted. Sequence is now: {seq}")
                except IndexOutOfBoundsError as e:
                    print(e)

            elif choice == 4:  # Remove
                try:
                    pos = int(input("Enter index to remove: "))
                except ValueError:
                    print("Invalid input for index.")
                    continue
                try:
                    if isinstance(seq, (ImmutableArraySequence, ImmutableListSequence)):
                        new_seq = seq.removeAt(pos)
                        self.sequences[idx] = new_seq
                        seq = new_seq
                        print(f"Removed. New sequence: {seq}")
                    else:
                        seq.removeAt(pos)
                        print(f"Removed. Sequence is now: {seq}")
                except IndexOutOfBoundsError as e:
                    print(e)

            elif choice == 5:  # Get item
                try:
                    pos = int(input("Enter index to get: "))
                except ValueError:
                    print("Invalid input for index.")
                    continue
                try:
                    value = seq.get(pos)
                    print(f"Item at index {pos}: {value}")
                except IndexOutOfBoundsError as e:
                    print(e)

            elif choice == 6:  # Get first
                try:
                    value = seq.getFirst()
                    print(f"First item: {value}")
                except IndexOutOfBoundsError as e:
                    print(e)

            elif choice == 7:  # Get last
                try:
                    value = seq.getLast()
                    print(f"Last item: {value}")
                except IndexOutOfBoundsError as e:
                    print(e)

            elif choice == 8:  # Subsequence
                try:
                    start = int(input("Enter start index: "))
                    end = int(input("Enter end index: "))
                except ValueError:
                    print("Invalid input for indices.")
                    continue
                try:
                    sub_seq = seq.getSubSequence(start, end)
                    print(f"Subsequence: {sub_seq}")
                except IndexOutOfBoundsError as e:
                    print(e)

            elif choice == 9:  # Print sequence
                print(f"Sequence: {seq}")
            else:
                print("Invalid choice. Please try again.")
