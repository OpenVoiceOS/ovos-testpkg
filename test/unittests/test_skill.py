import unittest
from ovos_testpkg import ReplaceSkillNameSkill
from ovos_bus_client import Message 
from ovos_utils.messagebus import FakeBus


class TestSkill(unittest.TestCase):
    def setUp(self):
        self.skill = ReplaceSkillNameSkill(bus=FakeBus(), skill_id="ovos_testpkg.openvoiceos")

    def test_skill(self):
        def custom_handle_homescreen(message):
            self.skill.bus.emit(message.reply("response"))

        self.skill.add_event("ovos_testpkg.openvoiceos.home", custom_handle_homescreen)
        msg = Message("ovos_testpkg.openvoiceos.home")
        response = self.skill.bus.wait_for_response(msg, "response")
        self.assertEqual(response.msg_type, "response")
