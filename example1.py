import textdistance as td

s1 = "kru"

s2 = "kru japanese cuisine"

normalized_levenstein = td.levenshtein.normalized_similarity(s1,s2)

print(normalized_levenstein)

# now for jaro

print(td.jaro_winkler(s1,s2))

