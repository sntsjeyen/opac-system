import multiprocessing as mp
import add_record as a
import edit_record as e
import delete_record as d
import view_records as v

class Menu:
    def mainMenu(all_records):
        try:
            choice = 1
            while choice != 6:
                print('''\nMAIN MENU
  [1] Add book record
  [2] Edit book record
  [3] Delete book record
  [4] View book records
  [5] Show book count summary
  [6] Exit''')
                choice = int(input("  >> Enter choice : "))
                if choice == 1:
                    a.addRecord(all_records)
                elif choice == 2:
                    e.editRecord(all_records)
                elif choice == 3:
                    d.deleteRecord(all_records)
                elif choice == 4:
                    v.viewRecords(all_records)
                elif (choice == 5) or (choice == 6):
                    return choice
                
        except:
            print(">>  An input error has occurred. Please try again.")
            Menu.mainMenu(all_records)

def computeBooksPerArea(all_records, queue):
    area0 = area1 = area2 = area3 = area4 = area5 = area6 = area7 = area8 = area9 = 0
    for acc_num, info in all_records.items():
        if (info[0] >= '000') and (info[0] < '100'):
            area0 += 1
        elif (info[0] >= '100') and (info[0] < '200'):
            area1 += 1
        elif (info[0] >= '200') and (info[0] < '300'):
            area2 += 1
        elif (info[0] >= '300') and (info[0] < '400'):
            area3 += 1
        elif (info[0] >= '400') and (info[0] < '500'):
            area4 += 1
        elif (info[0] >= '500') and (info[0] < '600'):
            area5 += 1
        elif (info[0] >= '600') and (info[0] < '700'):
            area6 += 1
        elif (info[0] >= '700') and (info[0] < '800'):
            area7 += 1
        elif (info[0] >= '800') and (info[0] < '900'):
            area8 += 1
        elif (info[0] >= '900') and (info[0] < '1000'):
            area9 += 1

    areas = {'General Works': area0, 'Philosophy and Psychology': area1,
             'Religion': area2, 'Social Sciences': area3,
             'Language': area4, 'Natural Sciences and Mathematics': area5,
             'Technology': area6, 'The Arts': area7,
             'Literature and Rhetoric': area8, 'History, Biography, and Geography': area9}
    
    queue.put(areas)

def computeNewlyAcquired(all_records, queue):
    new_count = 0
    for acc_num, info in all_records.items():
        if info[2] == "Yes":
            new_count += 1
    queue.put(new_count)

def computeToDiscard(all_records, queue):
    discard_count = 0
    for acc_num, info in all_records.items():
        if info[3] == "Yes":
            discard_count += 1
    queue.put(discard_count)

def computeDamaged(all_records, queue):
    damaged_count = 0
    for acc_num, info in all_records.items():
        if info[4] == "Damaged":
            damaged_count += 1
    queue.put(damaged_count)

def computeBorrowed(all_records, queue):
    borrowed_count = 0
    for acc_num, info in all_records.items():
        if info[5] == "Borrowed":
            borrowed_count += 1
    queue.put(borrowed_count)

def computeToReturn(all_records, queue):
    return_count = 0
    for acc_num, info in all_records.items():
        if info[5] == "To Return":
            return_count += 1
    queue.put(return_count)

if __name__ == '__main__':
    all_records = {}
    choice = 5
    print("\n=== WELCOME ===")
    while (choice == 5) and (choice != 6):
        choice = Menu.mainMenu(all_records)
        if choice == 6:
            exit(0)
        q = mp.Queue()

        c1 = mp.Process(target = computeBooksPerArea, args = (all_records, q))
        c2 = mp.Process(target = computeNewlyAcquired, args = (all_records, q))
        c3 = mp.Process(target = computeToDiscard, args = (all_records, q))
        c4 = mp.Process(target = computeDamaged, args = (all_records, q))
        c5 = mp.Process(target = computeBorrowed, args = (all_records, q))
        c6 = mp.Process(target = computeToReturn, args = (all_records, q))

        computations = [c1, c2, c3, c4, c5, c6]
        for c in computations:
            c.start()
            c.join()

        print("\n=== BOOK SUMMARY ===")
        print("\nBooks Per Area")
        for area, count in q.get().items():
            print('>> ' + area + ' : ' + str(count))
        print("Newly acquired books : " + str(q.get()))
        print("Books to be discarded : " + str(q.get()))
        print("Damaged books for repair : " + str(q.get()))
        print("Books borrowed : " + str(q.get()))
        print("Books to return : " + str(q.get()))
        print("\n=== BACK TO MAIN MENU ===")