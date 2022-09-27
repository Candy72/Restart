
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/login/{password}")
def login(password):
    if password == "12345678":
        return "Login successful."
    else:
        raise HTTPException(status_code=403, detail="Incorrect Password")
    
    