from unittest import TestCase
from kwil.types import TxPayloadType


class TestPayloadType(TestCase):
    def testString(self):
        self.assertEqual(str(TxPayloadType.DEPLOY_DATABASE), "DEPLOY_DATABASE")

    def testFormat(self):
        self.assertEqual(f'{TxPayloadType.DEPLOY_DATABASE}', "DEPLOY_DATABASE")
