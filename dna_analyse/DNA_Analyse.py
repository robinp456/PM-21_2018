# -*- coding: utf-8 -*-



from collections import Counter
gueltige_nukleotide = ['A', 'T', 'G', 'C']

# Molekulargewichte in mg/mol
# Nukleotidmonophosphate ohne 3'-OH-Gruppe
mw_a = 313210
mw_t = 304200
mw_g = 329210
mw_c = 289180
# freie OH-Gruppe am 3'-Ende eines DNA-Fragments
mw_oh = 17010


def ist_valide_sequenz(seq, alphabet, match_case=False):
    """Prüfe, ob eine Sequenz nur Buchstaben des erlaubten Alphabets enthält.
    Als Alphabet kann als iterierbare Buchstabenfolge beliebigen Typs
    übergeben werden.
    Mit match_case=True muss die Groß-/Kleinschreibung der des Alphabets
    entsprechen.
    """

    if match_case == False:
        # Groß-/Kleinschreibung soll keine Rolle spielen.
        # Deshalb wandeln wir die Sequenz und das Alphabet in Großbuchstaben
        # um. Für das Alphabet ist das am einfachsten, wenn wir es zuerst
        # in einen string verwandeln.
        seq = seq.upper()
        alphabet = ''.join(alphabet).upper()
    for c in seq:
        if c not in alphabet:
            return False
    return True


def hole_dna_sequenz(erlaubte_nukleotide):
    """Liefere eine vom Nutzer erfragte und validierte DNA-Sequenz.
    Um gültig zu sein, darf die Sequenz nur aus den Buchstaben
    aus erlaubte_nukleotide (in Groß- oder Kleinschreibung) bestehen.
    """

    while True:
        sequence = input('Gib eine DNA-Sequenz ein: ')

        if ist_valide_sequenz(sequence, erlaubte_nukleotide):
            return sequence

        # Dieser Teil wird ausgeführt wenn die Bedingung hinter if
        # nicht erfüllt war.
        print()
        print(
            'Bei der Eingabe handelt es sich nicht um eine gültige '
            'DNA-Sequenz!'
            )
        print()
        print()



if __name__ == '__main__':
    # Sequenz einlesen
    # ----------------
    seq = hole_dna_sequenz(gueltige_nukleotide)

    # Berechnungen
    # ------------

    # Sequenzlänge
    seqlen = len(seq)
    # Basenhäufigkeiten
    seq_dict = Counter(seq.upper())
    
    # GC-Gehalt
    gc_gehalt = 100 * (seq_dict['G']+seq_dict['C']) / seqlen
    # Molekulargewicht
    mw_gesamt = seq_dict['G']*mw_g + seq_dict['A']*mw_a + seq_dict['T']*mw_t + seq_dict['C']*mw_c + mw_oh  # in mg/mol

    complement = dict([('A', 'T'),('T', 'A'),('C', 'G'),('G', 'C')])
    compl_seq = ""
    for nucleotid in seq:
        compl_seq += complement[nucleotid.upper()]
    
    reversed_compl_seq = compl_seq[::-1]

    # Ausgabe
    # -------
    print()
    print('Eingelesene Sequenz:', seq)
    print()
    print('Länge:', seqlen)
    print()
    print('Base\tHäufigkeit')
    print('G', seq_dict['G'], sep='\t')
    print('A', seq_dict['A'], sep='\t')
    print('T', seq_dict['T'], sep='\t')
    print('C', seq_dict['C'], sep='\t')
    print()
    print('% GC-Gehalt:', gc_gehalt)
    print()
    print("Komplementärsequenz:", compl_seq, sep='\t')
    print()
    print("reverse Komplementärsequenz:", reversed_compl_seq, sep='\t')
    print()
    print('Molekulargewicht:', mw_gesamt/1000, 'g/mol')
