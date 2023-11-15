def remplacer_occurrences(chaine, ancien, nouveau):
    return chaine.replace(ancien, nouveau)

chaine_originale = "python programming"
ancien_caractere = "p"
nouveau_caractere = "P"
chaine_modifiee = remplacer_occurrences(chaine_originale, ancien_caractere, nouveau_caractere)
print(f"Chaine originale : {chaine_originale}")
print(f"Chaine modifiée : {chaine_modifiee}")
