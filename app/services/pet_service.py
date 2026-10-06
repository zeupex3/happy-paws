from app.repositories.pet_repository import (
    get_all_pets,
    get_pet_by_id,
    add_pet,
    update_pet,
    delete_pet,
)

def list_pets():
    pets = get_all_pets()
    return pets

def get_pet(pet_id):
    pet = get_pet_by_id(pet_id)
    return pet

def create_pet(name, pet_type, breed, age, owner_name):
    new_pet_id = add_pet(
        name,
        pet_type,
        breed,
        age,
        owner_name,
    )
    return new_pet_id

def update_pet_service(pet_id, name, pet_type, breed, age, owner_name):
    rows_updated = update_pet(
        pet_id,
        name,
        pet_type,
        breed,
        age,
        owner_name,
    )
    return rows_updated

def delete_pet_service(pet_id):
    rows_deleted = delete_pet(pet_id)
    return rows_deleted