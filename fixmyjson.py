from fix_busted_json import repair_json

badJson = '/home/marriott-2023-12-19T18 27 33Z.json'
outputJson = str(input("Please enter your new desired file name: ")) 

def fixJsonFile(inputFile, outputFile):
    try:
        with open(inputFile, 'r') as file:
            json = file.read()

        fixedJson = repair_json(json)

        with open(outputFile, 'w') as outputFile:
            outputFile.write(fixedJson)

        print(f"JSON properly formatted'{outputFile}'.")

    except FileNotFoundError:
        print(f"Error: File '{inputFile}' not found.")
    except Exception as e:
        print(f"[---] ERROR: \n\n{e}")



fixJsonFile(badJson, outputJson)
