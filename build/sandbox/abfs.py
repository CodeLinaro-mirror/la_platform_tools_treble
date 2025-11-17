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
import resource

def get_bind_mounts():
    bind_mounts = []
    home_dir = Path.home()
    if home_dir.exists():
        abfs_dir = home_dir/'.abfs'
        if abfs_dir.exists():
            bind_mounts.append(f'{abfs_dir.absolute()}')
            bind_mounts.append(f'{abfs_dir.absolute()}:/src/.abfs')
    return bind_mounts

def ensure_ulimit_nofile(min_limit=65536):
    """
    Check if limit of file read open is enough, and increase if not.
    """
    soft, hard = resource.getrlimit(resource.RLIMIT_NOFILE)
    if soft >= min_limit:
        return

    try:
        # Calculate new limit
        new_hard = max(hard, min_limit)

        # Apply new soft limit
        resource.setrlimit(resource.RLIMIT_NOFILE, (min_limit, new_hard))
        print(f" Successfully applied a new RLIMIT_NOFILE value: {min_limit, new_hard}")
    except ValueError as e:
        print(f" Failed to apply a new RLIMIT_NOFILE value: {e}")
    except Exception as e:
        print(f" Unexpected exception while applying a new value: {e}")