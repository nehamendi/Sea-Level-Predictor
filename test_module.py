import unittest
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend for testing
from sea_level_predictor import draw_plot

class TestSeaLevelPredictor(unittest.TestCase):

    def test_draw_plot_returns_figure(self):
        fig = draw_plot()
        self.assertIsNotNone(fig)
        self.assertEqual(type(fig).__name__, 'Figure')

    def test_plot_has_axes(self):
        fig = draw_plot()
        self.assertGreaterEqual(len(fig.axes), 1)

if __name__ == "__main__":
    unittest.main()