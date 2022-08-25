import sys
# import clipboard
# import clipboard
import clipboard
import json
saved_data = "clipboard.json"

# function to save data
def save_data(filepath, data):
    with open(filepath,"w") as f:
        json.dump(data,f)

# function to load saved data
def load_data(filepath):
    try:
        with open(filepath, "r") as f: 
            data = json.load(f)
            return data
    except:
        return {}

if len(sys.argv)==2:
    command = sys.argv[1]
    data = load_data(saved_data)

    if command == "save":
        key = input("Enter a key:")
        data[key] = clipboard.paste()
        save_data(saved_data,data)
        print("Data Saved!")
    elif command == "load":
        key = input("Enter a key:")
        if key in data:
            clipboard.copy(data[key])
            print("Data copied to clipboard")
        else:
            print("Enter a valid key!")
    elif command == "list":
        print(data)
    else:
        print("Unknown command")
else:
    print("Enter atleast one command")

        

