from main import VisitorsAnalyticsUtils
import unittest


class TestAdd(unittest.TestCase):
    def test_loadDataFile(self):
        self.assertEqual(
            VisitorsAnalyticsUtils().loadDataFile("./Int_Monthly_Visitor.csv").shape,
            (479, 35),
        )
        print("***unittest: loadDataFile passed***")


if __name__ == "__main__":
    unittest.main()
