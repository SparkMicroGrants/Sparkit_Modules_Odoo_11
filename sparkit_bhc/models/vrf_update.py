# -*- coding: utf-8 -*-
######################################################################################################
#
# Copyright (C) B.H.C. sprl - All Rights Reserved, http://www.bhc.be
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied,
# including but not limited to the implied warranties
# of merchantability and/or fitness for a particular purpose
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>
######################################################################################################

import logging
from odoo import models, fields, api ,_

_logger = logging.getLogger(__name__)


class SparkitVrf(models.Model):
    _inherit = 'sparkit.vrf'

    attendance_government_officials = fields.Integer('Government Officials in Attendace', default=0)
    created_on_ussd = fields.Boolean('Created on USSD', default=False, track_visibility='onchange')