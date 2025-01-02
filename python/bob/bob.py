def response(hey_bob):
    spaceless = ''.join(filter(lambda x: not x.isspace(), hey_bob))
    letters = ''.join(filter(str.isalpha, hey_bob))
    results = [len(letters)>0 and letters.upper() == letters, len(spaceless) > 0 and spaceless[-1] == "?", len(spaceless)==0]
    print(results)
    if results == [True, True, False]:
        return "Calm down, I know what I'm doing!"
    elif results == [False, True, False]:
        return "Sure."
    elif results == [True, False, False]:
        return "Whoa, chill out!"
    elif results == [False, False, True]:
        return "Fine. Be that way!"
    else:
        return "Whatever."

print(response("4?"))