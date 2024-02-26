motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")
motorcycles.remove(too_expensive)#두카티를 삭제
print(motorcycles)

motorcycles.sort()#영구정렬
print(motorcycles)
motorcycles.sorted()
print(sorted(motorcycles))
