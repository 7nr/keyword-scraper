import requests, os, threading

def writeResult(results: list):
    for result in results:
        if result == "":
            pass
        else:
            with open(f"results.txt", "a") as output:
                output.write(f"{result}\n")

def extractResult(text: str):
    resultStep = text.split(",[")[1]
    resultFinal = resultStep.replace('"', "").replace("]", "")
    xx = resultFinal.replace(",", "\n")
    if xx != "":
        print(xx)
    writeResult(results=list(resultFinal.split(",")))

def keywordRequest(baseKeyword: str):
    kReq = requests.get(f"https://suggestqueries.google.com/complete/search?jsonp=jQuery22408593668867170392_007741710334166862&q={baseKeyword}&client=chrome&_=0821810496179102")
    extractResult(str(kReq.text))

def setTitle():
    while True:
        try:
            file = open("results.txt", "r").read().splitlines()
            os.system(f"Title Keywords: {len(file)}")
        except:pass

def main():
    baseKeyword = str(input("Enter Starting Keyword: "))
    keywordRequest(baseKeyword)
    while True:
        file = open("results.txt", "r").read().splitlines()
        for keyword in file:
            keywordRequest(keyword)

if __name__ == "__main__":
    threading.Thread(target=setTitle).start()
    main()
