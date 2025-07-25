# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Utilities for ABFS-enabled builds."""
from pathlib import Path

def get_bind_mounts():
    bind_mounts = []
    home_dir = Path.home()
    if home_dir.exists():
        abfs_dir = home_dir/'.abfs'
        if abfs_dir.exists():
            bind_mounts.append(f'{abfs_dir.absolute()}')
    return bind_mounts