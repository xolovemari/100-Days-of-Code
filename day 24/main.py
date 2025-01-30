with open(r"C:\Users\marik\Projetos\100 days of python\day 24\Input\Names\invited_names.txt", "r") as name_file:
    all_names = [name.strip() for name in name_file.readlines()]

with open(r"C:\Users\marik\Projetos\100 days of python\day 24\Input\Letters\starting_letter.txt", "r") as letter_file:
    letter = letter_file.read()

for name in all_names:
    new_letter = letter.replace('[name]', name)
    safe_name = name.replace(" ", "_")
    letter_name = f"letter_for_{safe_name}.txt"
    caminho_novo_arquivo = fr"C:\Users\marik\Projetos\100 days of python\day 24\Output\ReadyToSend\{letter_name}"
    
    with open(caminho_novo_arquivo, "w") as output_file:
        output_file.write(new_letter)

    print(f"Carta criada para {name}: {letter_name}")