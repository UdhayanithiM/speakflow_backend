import re

def normalize(sentence: str):
    return re.findall(r"\w+", sentence.lower())


def validate_sentence(
    user_sentence: str,
    required_words: list,
    template: list,
    min_length: int
):
    tokens = normalize(user_sentence)

    # 1. Length check
    if len(tokens) < min_length:
        return False, "Sentence too short"

    # 2. Required keyword check
    for word in required_words:
        if word not in tokens:
            return False, f"Missing keyword: {word}"

    # 3. Order check (loose)
    template_index = 0
    for token in tokens:
        if template_index < len(template) and token == template[template_index]:
            template_index += 1

    if template_index < len(template) - 1:
        return False, "Incorrect word order"

    return True, "Correct sentence"
