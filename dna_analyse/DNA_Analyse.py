gueltige_nukleotide = ['A', 'T', 'G', 'C']

# Molekulargewichte in mg/mol
# Nukleotidmonophosphate ohne 3'-OH-Gruppe
mw_a = 313210
mw_t = 304200
mw_g = 329210
mw_c = 289180
# freie OH-Gruppe am 3'-Ende eines DNA-Fragments
mw_oh = 17010


def hole_dna_sequenz():
    """Liefere eine vom Nutzer erfragte und validierte DNA-Sequenz.
    Um gültig zu sein, darf die Sequenz nur aus den Buchstaben
    A, G, T, C, a, g, t, c bestehen.
    """

    # Hinweis: Verwende eine while-Schleife, innerhalb derer Du eine
    # Sequenz vom Nutzer erfragst und die Eingabe validierst.
    # Nur wenn die Validierung klappt, brichst Du die Schleife ab
    # und lieferst die Sequenz zurück.
    while True:
        sequence = input('Gib eine DNA-Sequenz ein: ')
        
        # Hier fehlt natürlich noch die Validierung.
        # Dafür brauchst Du noch eine Schleife, in der jeder Buchstabe
        # der Eingabe auf Gültigkeit geprüft werden muss.
        # Für einen Anfänger ist das schon eine ordentlich harte Nuss,
        # die aber mit etwas Anstrengung zu knacken sein sollte.
        for nucleotid in sequence:
            if nucleotid in gueltige_nukleotide:
                erfolgreiche_validierung= True
            elif nucleotid in [x.lower() for x in gueltige_nukleotide]:
                erfolgreiche_validierung= True
            else:
                erfolgreiche_validierung = False
                break
        if erfolgreiche_validierung:
            break
        else:
            # Dieser Teil wird ausgeführt wenn die Bedingung hinter if
            # nicht erfüllt war.
            print()
            print(
                'Bei der Eingabe handelt es sich nicht um eine gültige '
                'DNA-Sequenz!'
                )
            print()
            print()
        
    return sequence

def evaluate_sequence(sequence):
    a_count = 0
    c_count = 0
    g_count = 0
    t_count = 0
    for nucleotide in sequence:
        if nucleotide == 'A' or nucleotide == 'a':
            a_count = a_count + 1
        if nucleotide == 'C' or nucleotide == 'c':
            c_count = c_count + 1
        if nucleotide == 'G' or nucleotide == 'g':
            g_count = g_count + 1
        if nucleotide == 'T' or nucleotide == 't':
            t_count = t_count + 1
    print('Länge:\t',len(sequence))
    print('Base\\tHäufigkeit')
    print('A\t', a_count)
    print('C\t', c_count)
    print('G\t', g_count)
    print('T\t', t_count)
    print('%GC-Gehalt:\t', (c_count + g_count) / len(sequence))
    weigth = a_count*mw_a + g_count*mw_g + c_count*mw_c + t_count*mw_t + mw_oh
    print('Molekulargewicht:\t', weigth * 100)

seq = hole_dna_sequenz()

# Hier sollten jetzt die nötigen Berechnungen durchgeführt werden.

# Und hier erfolgt dann die Ausgabe.
print()
print('Eingelesene Sequenz: ', seq)
evaluate_sequence(seq)
