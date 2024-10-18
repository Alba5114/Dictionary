i = 1

dictionary = {
    "1": "Word registered with the serial number 1",
    "2": "Word registered with the serial number 2",
    "3": "Word registered with the serial number 3",
    "4": "Word registered with the serial number 4",
    "5": "Word registered with the serial number 5",
    "6": "Word registered with the serial number 6",
    "7": "Word registered with the serial number 7",
    "8": "Word registered with the serial number 8",
    "9": "Word registered with the serial number 9",
    "10": "Word registered with the serial number 10",
    "11.317940136293140164931024711442182814": "Word with an oddly specific serial number"
    
    
}
while i == 1:
    search = input("Awaiting input : ")
    if search in dictionary.keys():
        print("Entry found")
        print("Definition: " + dictionary[search] + " \n --------------------------------------------------------")
    else:
        print("We couldn't find an entry named '" + search + "', make sure your spelling is correct or search for another word" + "\n ----------------------------------------- ")
  
