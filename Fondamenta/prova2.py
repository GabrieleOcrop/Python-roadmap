import re

nome = "Gabriele"

check = re.findall(r'[^a-zA-Z0-9]', nome)

if check:
    print("blocca")
else:
    print("procedi")