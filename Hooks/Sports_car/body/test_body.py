from pytest import mark

@mark.body
class BodyTests:

    @mark.ui
    def test_navigation_as_expected(self):
        assert True

    def test_bumper_as_expected(self):
        assert True


    def test_windshielf(self):
        assert True