import random
from fastapi import FastAPI

app = FastAPI()



def get_quote(file):
    quote_list = []  # an empty list to store the quotes
    try:
        with open(file, "r") as quotefile:
            for line in quotefile:
                clean = line.strip()
                if clean:                  # skip blank/empty lines
                    quote_list.append(clean)
    except FileNotFoundError:
        print("Quotes file not found.")
    return quote_list

quotes = get_quote("quotes.txt")

@app.get("/")
def read_root():
    return{"message": "This is a random quotes api"}

@app.get("/quote")
def read_quote():
    if quotes:
        random_quote = random.choice(quotes)
        return {"quote": random_quote}
    else:
        return {"error": "No quotes available."}
    
    
       
    
     
