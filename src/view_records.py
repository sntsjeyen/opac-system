def viewRecords(all_records):
    if len(all_records) == 0:
        print(">> No record has been added yet.")
    else:
        key = 1
        for acc_num, info in all_records.items():
            print('\nRECORD #' + str(key))
            print('Accession Number : ' + str(acc_num))
            print('Call Number : ' + info[0])
            print('Book Title : ' + info[1])
            print('Newly Acquired : ' + info[2])
            print('To Be Discarded : ' + info[3])
            print('Condition : ' + info[4])
            print('Status : ' + info[5])
            key += 1
    print("\n=== BACK TO MAIN MENU ===")