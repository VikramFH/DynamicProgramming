def is_palindrome(subset_word):
    if subset_word==subset_word[::-1]:
        return True
    return False


def longest_subsequence_word(word):
    best = ""
    for left in range(len(word)):
        for right in range(left,len(word)):
            substring_word = s[left:rigth+1]
            if is_palindrome(substring_word) and len(substring_word) > len(best):
                best = substring_word

    return best

def longest_palindrome_word(word):
    best = ''

    for center in range(len(word)):
        left = center
        right = center

        while left>=0 and right<len(word) and word[left]==word[right]:
            left = left - 1
            right = right + 1

        left = left + 1
        right = right -1
        substring_word = word[left:right+1]

        if len(substring_word)>=len(best):
            best = substring_word

    return best

def padding_code(word):
    assert "!" not in word
    return "!".join(word)

def unpad_palindrome(word):
    return word.replace('!','')

def unpadded_length(padded):
    if not padded:
        return 0
    if padded[0]=='!':
        return len(padded-1)/2
    return len(padded+1)/2

def longest_palindrome_on2(s):

    padded_string = padding_code(s)
    best = ""
    for centre in range(len(s)):
        left = centre
        right = centre
        while left > 0 and right < len(s) and s[left]==s[right]:
            left = left - 1
            right = right + 1

        left = left + 1
        right = right - 1
        palindrome_word = s[left:right+1]

        if unpadded_length(palindrome_word)>unpadded_length(best):
            best = palindrome_word

    return unpad_palindrome(best)


# Def dynamic programming with O(n) There is a further optimization called the Mancher's algorithm. The intuition behind
# it is to remove the redundant expressions when the current palindrome defined is bigger than the existing palindrome

def longest_palindrome_on(s):
    padded_s = padding_code(s)
    best = ''
    best_right = -1
    best_center = -1
    #radius centre
    #radius[center]=best expansion radius found for the center
    radius = [0] * len(s)

    for center in range(len(s)):
        if center<=best_right:
            #Mancher Optimization:
            #The new center is inside the palindrome expansion from the earlier. We can skip the first steps of the
            # expansion, since they are equivalent to what we have already computed for the center's mirror.

            mirror = best_center - (center - best_center)
            radius[center] = min(best_right-center,radius[mirror])
        else:
            radius[center]=1

    left = center - radius[center]
    right = center - radius[center]
    while left>0 and right<lent(s)




