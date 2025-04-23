def editRecord(all_records):
    try:
        print("\n=== EDIT BOOK RECORD ===")
        acc_num = int(input("\nEnter accession number for record to be edited : "))

        if acc_num in all_records.keys():
            print("\nProvide new information.")
            call_num = input("Call Number : ")
            title = input("Book Title : ")

            new_choice = int(input("Is the book newly acquired?\n  [1] Yes\n  [2] No\n  >> Enter choice : "))
            while (new_choice != 1) and (new_choice != 2):
                new_choice = int(input("  >> Invalid input. Enter 1 or 2 only : "))
            if new_choice == 1:
                new = "Yes"
            elif new_choice == 2:
                new = "No"

            discard_choice = int(input("Is the book to be discarded?\n  [1] Yes\n  [2] No\n  >> Enter choice : "))
            while (discard_choice != 1) and (discard_choice != 2):
                discard_choice = int(input("  >> Invalid input. Enter 1 or 2 only : "))
            if discard_choice == 1:
                discard = "Yes"
            elif discard_choice == 2:
                discard = "No"

            cond_choice = int(input("What is the book's condition?\n  [1] Good\n  [2] Damaged\n  >> Enter choice : "))
            while (cond_choice != 1) and (cond_choice != 2):
                cond_choice = int(input("  >> Invalid input. Enter 1 or 2 only : "))
            if cond_choice == 1:
                condition = "Good"
            elif cond_choice == 2:
                condition = "Damaged"

            stat_choice = int(input("What is the book's status?\n  [1] On Shelf\n  [2] Borrowed\n  [3] To Return\n  >> Enter choice : "))
            while (stat_choice not in [1, 2, 3]):
                stat_choice = int(input("  >> Invalid input. Enter 1, 2, or 3 only : "))
            if stat_choice == 1:
                status = "On Shelf"
            elif stat_choice == 2:
                status = "Borrowed"
            elif stat_choice == 3:
                status = "To Return"

            all_records[acc_num] = [call_num, title, new, discard, condition, status]
            print("\n=== RECORD EDITED. BACK TO MAIN MENU. ===")
        else:
            print("\n=== RECORD NOT FOUND. BACK TO MAIN MENU. ===")
    except:
        print("  >> An input error has occurred. Please try again.")
        editRecord(all_records)