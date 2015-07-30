test2

from website.addons.base import AddonUserSettingsBase, AddonNodeSettingsBase
from framework import GuidStoredObject
from framework import fields
import datetime
import markdown

class AddonRtmilkNodeSettings(AddonNodeSettingsBase):
    def to_json(self, user):
        return {}

class NodeRtmilkPage(GuidStoredObject):

    redirect_mode = 'redirect'

    _id = fields.StringField(primary=True)

    page_name = fields.StringField()
    version = fields.IntegerField()
    date = fields.DateTimeField(auto_now_add=datetime.datetime.utcnow)
    is_current = fields.BooleanField()
    content = fields.StringField()

    user = fields.ForeignField('user')
    node = fields.ForeignField('node')
