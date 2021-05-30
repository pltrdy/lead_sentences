import sys


SENTENCE_BREAKS = [
    ".",
    "!",
    "?",
]
def count_sentences(sequence, sentence_breaks=SENTENCE_BREAKS):
    prev_spe_char = False
    words = sequence.split()
    sentences = []
    n = 0

    for word in words:
        if word in sentence_breaks:
            if not prev_spe_char:
                # break the sentence
                prev_spe_char = True
                n += 1

            else:
                # append spe char to previous sentence
                prev_spe_char = True
        else:
            prev_spe_char = False
    if not prev_spe_char:
        # Consider a sentence even if it has no end period
        n += 1
    return n


def path_lead_n(path, out_path=None, n=3, lead_reference_path=None):
    if out_path is None:
        out = None
    else:
        out = open(out_path, 'w')

    def _file_iterator(f, reference_iterator):
        for line, reference in zip(f, reference_iterator):
            line = line.strip()

            yield (line, reference,)

    def _reference_iterator(lead_reference_path):
        if lead_reference_path is None:
            while True:
                yield None
        else:
            with open(lead_reference_path) as f:
                for line in f:
                    line = line.strip()

                    yield line


    with open(path) as f:
        ref_it = _reference_iterator(lead_reference_path)
        it = _file_iterator(f, ref_it)
        return lead_n(it, n=n, out=out)


def lead_n(iterator, n=3, out=None,
           sentence_breaks=SENTENCE_BREAKS):
    
    results = []
    def output_or_store(s):
        if out is not None:
            print(s, file=out)
        results.append(s)

    for i, (sequence, reference) in enumerate(iterator):
        if reference is not None:
            n = count_sentences(reference, sentence_breaks=sentence_breaks)
            # print(reference)
            # print("Lead Oracle %d: %d" % (i, n))
        prev_spe_char = False
        words = sequence.split()
        cur_sentence = []
        sentences = []
        seq_n = 0

        for word in words:
            if word in sentence_breaks:
                if not prev_spe_char:
                    # break the sentence
                    cur_sentence.append(word)
                    sentences.append(cur_sentence)
                    cur_sentence = []
                    prev_spe_char = True
                    seq_n += 1

                else:
                    # append spe char to previous sentence
                    sentences[-1].append(word)
                    prev_spe_char = True
            else:
                if seq_n >= n:
                    break
                prev_spe_char = False
                cur_sentence.append(word)

        if seq_n < n:
            # might be the case if there's not enough sentences
            # or last sentence does not contain period
            if len(cur_sentence) > 0:
                sentences.append(cur_sentence)
        lead_n_text = " ".join([" ".join(s) for s in sentences])
        output_or_store(lead_n_text)


    return results
