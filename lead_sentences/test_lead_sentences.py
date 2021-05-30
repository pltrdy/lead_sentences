import lead_sentences

def main():
    sequences = [
        "haha hoho . hihi juju ! jaja ! ! !",
        "aa , bb , bb ! ? jiji . jaja ! ",
    ]
    print(lead_sentences.lead_n(sequences, n=3))

if __name__ == "__main__":
    main()
