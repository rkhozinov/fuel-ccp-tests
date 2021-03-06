#    Copyright 2016 Mirantis, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
import os

import pytest

from fuel_ccp_tests import settings_oslo


@pytest.fixture(scope='session')
def config():

    config_files = []

    tests_configs = os.environ.get('TESTS_CONFIGS', None)
    if tests_configs:
        for test_config in tests_configs.split(','):
            config_files.append(test_config)

    config_opts = settings_oslo.load_config(config_files)

    return config_opts
