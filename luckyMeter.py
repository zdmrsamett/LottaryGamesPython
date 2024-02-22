import random

rate = random.randint(0, 100)

if 0 <= rate <= 25:
    print(f"Şansınız: % {rate} Şansınız çok kötü, risk almayın.")
elif 25 < rate <= 50:
    print(f"Şansınız: % {rate} Şansınız kötü, ciddi kararlardan uzak durun.")
elif 50 < rate <= 75:
    print(f"Şansınız: % {rate} Şansınız normal.")
elif 75 < rate <= 100:
    print(f"Şansınız: % {rate} Şansınız mükemmel, hadi piyango bileti alalım.")
