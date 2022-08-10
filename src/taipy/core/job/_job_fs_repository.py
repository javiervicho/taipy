# Copyright 2022 Avaiga Private Limited
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
# an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.
import pathlib
from typing import Optional

from .. import Job
from ._job_model import _JobModel
from ._job_repository import _JobRepository


class _JobFSRepository(_JobRepository):
    def __init__(self):
        super().__init__(model=_JobModel, dir_name="jobs")

    @property
    def dir_path(self):
        return super().repo.dir_path

    @property
    def _storage_folder(self) -> pathlib.Path:
        return super().repo._storage_folder

    def _get_by_config_and_parent_id(self, config_id: str, parent_id: Optional[str]) -> Optional[Job]:
        return super().repo._get_by_config_and_parent_id(config_id, parent_id)

    def _get_by_configs_and_parent_ids(self, configs_and_parent_ids):
        return super().repo._get_by_configs_and_parent_ids(configs_and_parent_ids)

    def __match_file_and_get_entity(self, filepath, config_and_parent_ids, retry: Optional[int] = 0):
        return super().repo.__match_file_and_get_entity(filepath, config_and_parent_ids, retry)
