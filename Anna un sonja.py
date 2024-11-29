import math

# Funkcija, kas veic ievadīto skaitļu šķirošanu (Insertion Sort)
def insertion_sort(arr):
    """
    Funkcija šķiro ievadītos skaitļus augošā secībā, izmantojot Insertion Sort algoritmu.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Funkcija, kas aprēķina vidējo vērtību (aritmētisko vidējo)
def calculate_mean(arr):
    """
    Funkcija aprēķina vidējo vērtību (aritmētisko vidējo).
    """
    if len(arr) == 0:
        return 0
    return sum(arr) / len(arr)

# Funkcija, kas aprēķina mediānu
def calculate_median(arr):
    """
    Funkcija aprēķina mediānu (vidējo vērtību pēc šķirošanas).
    """
    n = len(arr)
    insertion_sort(arr)  # Pārliecināmies, ka masīvs ir sakārtots
    if n % 2 == 0:
        return (arr[n // 2 - 1] + arr[n // 2]) / 2
    else:
        return arr[n // 2]
    
# Funkcija, kas aprēķina vismazāko skaitli
def find_min(arr):
    """
    Funkcija atgriež vismazāko skaitli masīvā.
    """
    return min(arr)

# Funkcija, kas aprēķina lielāko skaitli
def find_max(arr):
    """
    Funkcija atgriež lielāko skaitli masīvā.
    """
    return max(arr)

# Funkcija, kas aprēķina skaitļu summu
def calculate_sum(arr):
    """
    Funkcija aprēķina skaitļu summu masīvā.
    """
    return sum(arr)

# Funkcija, kas izvada masīvu
def print_array(arr):
    """
    Funkcija izvada masīvu.
    """
    for num in arr:
        print(num, end=" ")
    print()

# Funkcija, kas izvada statistikas rezultātus
def print_statistics(arr):
    """
    Funkcija izvada visu analīzi: vidējo vērtību, mediānu, varianci, standartnovirzi,
    kā arī vismazāko un lielāko skaitli.
    """
    if len(arr) == 0:
        print("Masīvs ir tukšs.")
        return
    
    mean = calculate_mean(arr)
    median = calculate_median(arr)
    min_val = find_min(arr)
    max_val = find_max(arr)
    total_sum = calculate_sum(arr)

    print("Analīze par ievadītajiem skaitļiem:")
    print(f"Vidējā vērtība: {mean}")
    print(f"Mediāna: {median}")
    print(f"Vismazākais skaitlis: {min_val}")
    print(f"Lielākais skaitlis: {max_val}")
    print(f"Skaitļu summa: {total_sum}")

# Galvenā programma
if __name__ == "__main__":
    # Lietotāja ievads
    print("Sveiki! Šī programma analizēs Jūsu ievadītos skaitļus.")
    user_input = input("Ievadiet skaitļus, atdalītus ar atstarpēm: ").split()
    
    # Pārvēršam ievadītos skaitļus par veseliem skaitļiem
    try:
        user_input = [int(i) for i in user_input]
    except ValueError:
        print("Lūdzu, ievadiet tikai skaitļus.")
        exit()

    # Ja masīvs ir tukšs, izdrukājam atbilstošu ziņojumu
    if len(user_input) == 0:
        print("Masīvs ir tukšs, nevar veikt analīzi.")
    else:
        # Parādām ievadītos skaitļus un pēc tam analizējam tos
        print("Ievadītie skaitļi ir: ", end="")
        print_array(user_input)
        
        # Šķirojam skaitļus
        insertion_sort(user_input)
        
        # Izvada sakārtotās vērtības
        print("Sakārtotie skaitļi: ", end="")
        print_array(user_input)
        
        # Veicam analīzi
        print_statistics(user_input)
