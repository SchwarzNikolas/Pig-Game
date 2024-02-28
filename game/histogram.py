"""The Module to display Highscore graphically."""


class Histogram:
    """Blueprint for a Histogram."""
    
    def barchart(self):
        number = 10
        print(f"{'∎' * number} -> {number}") 


histogram = Histogram()
histogram.barchart()
