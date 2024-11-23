def filtrar_livros(lista_json):
    def validar_livro(livro):
        subjects = livro.get("subjects", [])

        if any("Poetry" in subject for subject in subjects):
            return False

        has_fiction = any("Fiction" in subject for subject in subjects)
        has_philosophy = any("Philosophy" in subject for subject in subjects)

        if has_fiction and has_philosophy:
            return False
        if not (has_fiction or has_philosophy):
            return False

        return True

    return [livro for livro in lista_json if validar_livro(livro)]