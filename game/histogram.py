"""The Module to display Highscore graphically."""


class Histogram:
    """Blueprint for a Histogram."""
    
    def barchart(self):
        number = 10
        player_name = "isaac"
        print(f"{player_name} | 
        
              {'∎' * number}{number}") 


histogram = Histogram()
histogram.barchart()
