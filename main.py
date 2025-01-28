from fastapi import FastAPI

import user.router as router
app = FastAPI()

app.include_router(router.router)

@app.get("/")
def read_root():
    return {"message":"hey server is up and running!"}
    


    

    
