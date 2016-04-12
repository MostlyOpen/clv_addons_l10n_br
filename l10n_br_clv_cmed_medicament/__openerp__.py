# -*- coding: utf-8 -*-
###############################################################################
#
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

{
    'name': 'CMED Medicament',
    'summary': 'CMED Module used in CLVsol Solutions.',
    'version': '2.0',
    'author': 'Carlos Eduardo Vercelino - CLVsol',
    'category': 'Generic Modules/Others',
    'license': 'AGPL-3',
    'website': 'http://clvsol.com',
    'images': [],
    'depends': [
        'clv_medicament',
        ],
    'data': [
        'security/clv_cmed_medicament_security.xml',
        'security/ir.model.access.csv',
        'clv_cmed_medicament_view.xml',
        # 'tag/clv_tag_view.xml',
        # 'annotation/clv_annotation_view.xml',
        'cmed_list/clv_cmed_medicament_list_view.xml',
        'cmed_list/clv_cmed_medicament_list_item_view.xml',
        'menu/clv_cmed_medicament_menu_view.xml',
        ],
    'demo': [],
    'test': [],
    'init_xml': [],
    'test': [],
    'update_xml': [],
    'installable': True,
    'application': False,
    'active': False,
    'css': [],
}
