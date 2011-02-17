from simplesite.tests import *

class TestPageController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='page', action='index'))
        # Test response...
    
    def test_view(self):
        response = self.app.get(url(controller='page', action='view', id=1))
        assert 'Home' in response
        assert 'REQUEST_METHOD' in response.req.environ