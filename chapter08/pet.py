def describe_pet( animal_type, pet_name):
    """반려동물 정보를 표시합니다."""
    print(f"\n I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
    
describe_pet('hamster', 'harry')

describe_pet(pet_name='marry', animal_type='cat')
