def validate_json_list(data_list):
    if not isinstance(data_list, list):
        raise ValueError("A entrada deve ser uma lista.")

    def validate_item(data):
        subjects = data.get("subjects", [])

        if not isinstance(subjects, list):
            return False

        contains_poetry = "Poetry" in subjects
        contains_fiction = "Fiction" in subjects
        contains_philosophy = "Philosophy" in subjects

        if contains_poetry:
            return False
        if not (contains_fiction or contains_philosophy):
            return False
        if contains_fiction and contains_philosophy:
            return False

        return True
    
    return [validate_item(item) for item in data_list]