# (C) Datadog, Inc. 2018
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
from .constants import get_root
from ..subprocess import run_command

STYLE_ENVS = (
    'flake8',
)


def get_tox_envs(check, sorted=False):
    env_list = run_command('tox --listenvs', capture='out').stdout
    env_list = [e.strip() for e in env_list.splitlines()]

    if sorted:
        env_list.sort()

        # Put benchmarks after regular test envs
        benchmark_envs = []

        for e in env_list:
            if 'bench' in e:
                benchmark_envs.append(e)

        # Put style checks at the end always
        for style_type in STYLE_ENVS:
            try:
                env_list.remove(style_type)
                env_list.append(style_type)
            except ValueError:
                pass

    return env_list
