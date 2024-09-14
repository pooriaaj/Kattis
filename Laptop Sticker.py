margin = 1
Lw, Lh, Sw, Sh = map(int, input().split())
willfithorizontally = margin + margin + Sw <= Lw
willfitvertically = margin + margin + Sh <= Lh
willfit = willfithorizontally and willfitvertically
print(1 if willfit else 0)
