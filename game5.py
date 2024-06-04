import random

def main():
    #Mula permainan teka
    print("++++++++++++++++++++++++++++++++++")
    print("     Guess Traditional Game       ")
    print("++++++++++++++++++++++++++++++++++\n")
    
    #Pilihan permainan tradisional
    soalan_kuiz = [
    "Traditional game that involves at least 2 players or more. It is usually played with few small round stones or pebbles.\n(A) Gasing\n(B) Batu Seramban\n(C) Ceper\n(D) Guli",
    "Played with two players sitting in front of one another.\n(A) Congkak\n(B) Gasing\n(C) Guli\n(D) Ceper",
    "This game uses bottle caps.\n(A) Guli\n(B) Gasing\n(C) Ceper\n(D) Batu seremban"
]

    for i in range (2):
        # Pilih soalan secara rawak
        soalan_rawak = random.choice(soalan_kuiz)
        
        # Cetak soalan yang dipilih
        print(soalan_rawak)
    
        jawapan_betul = ["b", "a", "c"]

        # Memeriksa jawapan pemain
        jawapan_pemain = input("Answer: ")

        if jawapan_pemain.lower() == jawapan_betul[soalan_kuiz.index(soalan_rawak)]:
            print("CORRECT! GOOD JOB!\n")
        else:
            print("INCORRECT!")
            print("THE CORRECT ANSWER IS", jawapan_betul[soalan_kuiz.index(soalan_rawak)], "\n\n")

    else:
        print("Thank you")    
        
main()