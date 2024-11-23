def filtrar_livros(lista_json, subject_counter, books_minimum):
    def validar_livro(livro):
        subjects = livro.get("subjects", [])

        if any("poetry" in subject.lower() for subject in subjects):
            return False

        has_fiction = any("fiction" in subject.lower() for subject in subjects)
        has_philosophy = any("philosophy" in subject.lower() for subject in subjects)

        if has_fiction and has_philosophy:
            return False
        if not (has_fiction or has_philosophy):
            return False
        
        livro_subject = 'fiction' if has_fiction else 'philosophy'
        if(subject_counter[livro_subject] >= books_minimum):
            return False
        
        livro['validated_subject'] = livro_subject
        subject_counter[livro_subject] += 1 
        return True

    return [livro for livro in lista_json if validar_livro(livro)]