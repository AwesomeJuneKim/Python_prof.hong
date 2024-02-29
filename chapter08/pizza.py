def make_pizza(size, *toppings):
    """요청받은 토핑 리스트를 출력합니다."""
    print(f"size={size}")
    for topping in toppings:
        print(f"- {topping}")
    


