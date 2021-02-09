from django.contrib.staticfiles import finders
from django.test import TestCase


MISSING_ASSET = 'Frontend asset "%s" missing. Did you build it?'

ASSETS = [
    'tellme/feedback/dist/feedback.js',
    'tellme/feedback/dist/feedback.css',
]


class AssetTests(TestCase):
    def test_assets_exist(self):
        for asset in ASSETS:
            with self.subTest(asset=asset)
                result = finders.find(asset)
                self.assertTrue(result, MISSING_ASSET % asset)
