conjunto1união = {2, 8, "a", 5}

conjunto2união = {7, 9, 2, "b", 6, 8}

uniao = conjunto1união.union(conjunto2união)

conjunto1inter = {5, 7, 8, 9}

conjunto2inter = {7, 2, 1, 9, 3}

interseção = conjunto1inter.intersection(conjunto2inter)

conjunto1dife = {1, 2, 3, 7, 8, "v"}

conjunto2dife = {3, 7, 1, 2}

diferença = conjunto1dife - conjunto2dife

conjunto1cartesiano = {1, 3, 5}

conjunto2cartesiano = {3, 4, 6}

cartesiano = []

for a in conjunto1cartesiano:
  for b in conjunto2cartesiano:
    cartesiano.append((a, b))

print("4")

print("U")

print("conjunto U A:", conjunto1união)

print("conjunto U B:", conjunto2união)

print("I")

print("conjunto I A:", conjunto1inter)

print("conjunto I B:", conjunto2inter)

print("D")

print("conjunto D A:", conjunto1dife)

print("conjunto D B:", conjunto2dife)

print("C")

print("conjunto C A:", conjunto1cartesiano)

print("conjunto C B:", conjunto2cartesiano)

print("União: conjunto 1", conjunto1união, "conjunto 2", conjunto2união,
      "resultado:", uniao)

print("Interseção: conjunto 1", conjunto1inter, "conjunto 2", conjunto2inter,
      "resultado:", interseção)

print("Diferença: conjunto 1", conjunto1dife, "conjunto 2", conjunto2dife,
      "resultado:", diferença)

print("Produto Cartesiano: conjunto 1", conjunto1cartesiano, "conjunto 2",
      conjunto2cartesiano, "resultado:", cartesiano)