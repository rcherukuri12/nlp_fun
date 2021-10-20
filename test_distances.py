import nltk
import nltk.metrics.distance

def demo():
    string_distance_examples = [
        ("rain", "shine"),
        ("abcdef", "acbdef"),
        ("language", "lnaguaeg"),
        ("language", "lnaugage"),
        ("language", "lngauage"),
    ]
    for s1, s2 in string_distance_examples:
        print("Edit distance btwn '%s' and '%s':" % (s1, s2), edit_distance(s1, s2))
        print(
            "Edit dist with transpositions btwn '%s' and '%s':" % (s1, s2),
            edit_distance(s1, s2, transpositions=True),
        )
        print("Jaro similarity btwn '%s' and '%s':" % (s1, s2), jaro_similarity(s1, s2))
        print(
            "Jaro-Winkler similarity btwn '%s' and '%s':" % (s1, s2),
            jaro_winkler_similarity(s1, s2),
        )
        print(
            "Jaro-Winkler distance btwn '%s' and '%s':" % (s1, s2),
            1 - jaro_winkler_similarity(s1, s2),
        )
    s1 = set([1, 2, 3, 4])
    s2 = set([3, 4, 5])
    print("s1:", s1)
    print("s2:", s2)
    print("Binary distance:", binary_distance(s1, s2))
    print("Jaccard distance:", jaccard_distance(s1, s2))
    print("MASI distance:", masi_distance(s1, s2))



if __name__ == "__main__":
    demo()

  
