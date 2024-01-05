import statistics
import collections


class GrowthTimeStats:
    
    def __init__(self, growth_times: list[int]):
        """
        A class to calculate statistics from a list of integer growth times.
        """
        self.growth_times = sorted(growth_times)

    def _round(self, number):
        return float(f"{number:.2f}")

    def get_min(self):
        return self.growth_times[0]

    def get_max(self):
        return self.growth_times[-1]

    def get_mean(self):
        return self._round(statistics.mean(self.growth_times))
    
    def get_median(self):
        return self._round(statistics.median(self.growth_times))
    
    def get_variance(self):
        return self._round(statistics.variance(self.growth_times))
    
    def get_frequency(self):
        return dict(collections.Counter(self.growth_times))