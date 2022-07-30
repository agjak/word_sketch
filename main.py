

from .word_sketch import parse_corpus, search_in_parsed_corpus, common_collocations_in_parsed_corpus
def main():
    #word_sketch.tag_corpus("files/tmp/paths.txt","files/corpora/OANC_written_en.txt","en")

    parse_corpus("word_sketch/files/corpora/aktualnosci_uw_pl.vert", "word_sketch/files/grammars/IPI_PAN_1.1_pl.txt","word_sketch/files/parsed_corpora/aktualnosci_uw_IPI_PAN_1.1_pl.p")
    parse_corpus("word_sketch/files/corpora/OANC_spoken_en.txt", "word_sketch/files/grammars/penn_3.1_en.txt","word_sketch/files/parsed_corpora/OANC_spoken_penn_3.1_en.p")


    common_collocations_in_parsed_corpus("word_sketch/files/parsed_corpora/aktualnosci_uw_IPI_PAN_1.1_pl.p","uniwersytet","uczelnia",4)
    common_collocations_in_parsed_corpus("word_sketch/files/parsed_corpora/OANC_spoken_penn_3.1_en.p","be","have",amount=4)

    search_in_parsed_corpus("word_sketch/files/parsed_corpora/aktualnosci_uw_IPI_PAN_1.1_pl.p", "uniwersytet", 12)
    search_in_parsed_corpus("word_sketch/files/parsed_corpora/OANC_spoken_penn_3.1_en.p", "be", amount=12)

    parse_corpus("word_sketch/files/KPWr/00100622.xml", "word_sketch/files/grammars/IPI_PAN_1.1_pl.txt","word_sketch/files/parsed_corpora/KPWR_test.p",KPWr=True)
    search_in_parsed_corpus("word_sketch/files/parsed_corpora/KPWR_test.p", "problem", amount=12)

if __name__ == "__main__":
    main()