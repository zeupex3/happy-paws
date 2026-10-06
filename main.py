from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.services.pet_service import list_pets, get_pet, create_pet, delete_pet_service

app = FastAPI(title="Happy Paws API")

class PetCreate(BaseModel):
    name: str
    type: str
    breed: str
    age: int
    owner_name: str

@app.get("/pets")
def read_all_pets():
    return list_pets()

@app.get("/pets/{pet_id}")
def read_pet(pet_id: int):
    pet = get_pet(pet_id)
    if not pet:
        raise HTTPException(status_code=404, detail="Pet not found")
    return pet

@app.post("/pets")
def add_new_pet(pet: PetCreate):
    new_id = create_pet(pet.name, pet.type, pet.breed, pet.age, pet.owner_name)
    return {"message": "Pet added successfully", "id": new_id}

@app.delete("/pets/{pet_id}")
def remove_pet(pet_id: int):
    deleted_rows = delete_pet_service(pet_id)
    if deleted_rows == 0:
        raise HTTPException(status_code=404, detail="Pet not found")
    return {"message": "Pet deleted"}