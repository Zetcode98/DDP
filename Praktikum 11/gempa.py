class Gempa:
    def __init__(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala
    
    def dampak(self):
        if self.skala < 2:
            return "Dampak gempa tidak berasa"
        elif self.skala >= 2 and self.skala <= 4:
            return "Dampak gempa bangunan retak-retak"
        elif self.skala >= 4 and self.skala <= 6:
            return "Dampak gempa bangunan roboh"
        else:
            return "Dampak gempa bangunan roboh dan berpotensi tsunami"

