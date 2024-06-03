# 将一些想去旅游的地方存储在一个列表中
places_to_visit = ["Kyoto", "New York", "Paris", "Sydney", "Cape Town"]
# 按原始排列顺序打印该列表
print("原始列表：")
print(places_to_visit)

# 使用 sorted() 按字母顺序打印这个列表，不要修改它
print("\n按字母顺序排列（不修改原列表）：")
print(sorted(places_to_visit))

# 再次打印该列表，核实排列顺序未变
print("\n再次打印原始列表，核实未变：")
print(places_to_visit)

# 使用 sorted() 按与字母顺序相反的顺序打印这个列表，不要修改它
print("\n按与字母顺序相反的顺序排列（不修改原列表）：")
print(sorted(places_to_visit, reverse=True))

# 再次打印该列表，核实排列顺序未变
print("\n再次打印原始列表，核实未变：")
print(places_to_visit)

# 使用 reverse() 修改列表元素的排列顺序
places_to_visit.reverse()
print("\n使用 reverse() 修改排列顺序：")
print(places_to_visit)

# 使用 reverse() 再次修改列表元素的排列顺序
places_to_visit.reverse()
print("\n使用 reverse() 恢复原来的排列顺序：")
print(places_to_visit)

# 使用 sort() 修改该列表，使其元素按字母顺序排列
places_to_visit.sort()
print("\n使用 sort() 按字母顺序排列：")
print(places_to_visit)

# 使用 sort() 修改该列表，使其元素按与字母顺序相反的顺序排列
places_to_visit.sort(reverse=True)
print("\n使用 sort() 按与字母顺序相反的顺序排列：")
print(places_to_visit)
