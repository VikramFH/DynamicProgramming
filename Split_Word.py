import collections

def split_word(dictionary,sentences):

    prefixes_to_process = collections.deque([])
    split_dict = {"":[]}

    while prefixes_to_process:
        prefix = prefixes_to_process.popleft()
        if prefix==sentences:
            return split_dict[prefix]

        for word in dictionary:
            if sentences[len(prefix):].startswith(word):
                next_prefix = prefix + word
                if next_prefix not in prefixes_to_process:
                    split_dict[next_prefix] = split_dict[prefix] + [word]
                    prefixes_to_process.append(next_prefix)

    return None