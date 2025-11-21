from tpa.collatz import *

seed: int = 1999
index: int = collatz_lifetime(seed)
# series: list[int] = co.collatz_series(seed, index)
height: int = collatz_altitude(seed)

print(f"La suite de collatz pour N={seed}"
      f" a une duree de vie de {index}, une altitude de {height}\n"
      # f"et ses premiers termes sont {series[:10]}"
)