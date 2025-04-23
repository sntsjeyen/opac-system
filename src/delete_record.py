def deleteRecord(all_records):
    try:
        print('\n=== DELETE BOOK RECORD ===')
        acc_num = int(input("\nInput accession number of book record to be deleted: "))
        if acc_num in all_records.keys():
            del all_records[acc_num]
            print("\n=== RECORD HAS BEEN DELETED. BACK TO MAIN MENU. ===")
        else:
            print("\n=== RECORD NOT FOUND. BACK TO MAIN MENU. ===")
    except:
        print("  >> An input error has occurred. Please try again.")
        deleteRecord(all_records)